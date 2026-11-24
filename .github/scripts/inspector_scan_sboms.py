"""Scan PR-built SBOMs with the Amazon Inspector Scan API.

Runs in the trusted inspector-pr-scan workflow. The SBOM artifacts come from a
pull_request run and are treated as untrusted data: they are only parsed as
JSON and passed to the AWS CLI as a file; nothing in them is executed.

Usage: inspector_scan_sboms.py <artifact_dir> <expected_head_sha>
Writes summary.md and result.json to the current directory.
"""

import json
import os
import pathlib
import subprocess
import sys

MAX_SBOM_BYTES = 50 * 1024 * 1024
COUNTED = ("critical", "high")
MARKER = "<!-- amazon-inspector-pr-scan -->"


def inspector_severity(vuln):
    for rating in vuln.get("ratings", []):
        if rating.get("source", {}).get("name") == "AMAZON_INSPECTOR":
            return str(rating.get("severity", "unknown")).lower()
    return "unknown"


CHUNK = 100


def _scan_file(path):
    proc = subprocess.run(
        [
            "aws", "inspector-scan", "scan-sbom",
            "--sbom", f"file://{path}",
            "--output-format", "CYCLONE_DX_1_5",
        ],
        capture_output=True, text=True,
    )
    if proc.returncode:
        if "Response too large" in proc.stderr:
            return None
        raise RuntimeError(proc.stderr)
    doc = json.loads(proc.stdout)
    return doc.get("sbom", doc)


def scan(path):
    """Scan in component chunks: a whole image (e.g. nodejs20.x) can exceed the
    API's response size. Chunks that are still too large are split in half; a
    single component that is too large on its own is reported as skipped."""
    sbom = json.loads(pathlib.Path(path).read_text())
    base = {k: v for k, v in sbom.items() if k not in ("components", "dependencies")}
    base["metadata"] = {k: v for k, v in sbom.get("metadata", {}).items() if k != "component"}
    tmp = pathlib.Path(f"{path}.part.json")
    merged = {"components": [], "vulnerabilities": [], "skipped": []}

    def run(chunk, n=[0]):
        tmp.write_text(json.dumps(dict(base, components=chunk)))
        result = _scan_file(tmp)
        if result is None:
            if len(chunk) == 1:
                merged["skipped"].append(chunk[0].get("purl") or chunk[0].get("name"))
                return
            half = len(chunk) // 2
            run(chunk[:half])
            run(chunk[half:])
            return
        # bom-refs are only unique within one response, so prefix them per chunk
        n[0] += 1
        prefix = f"c{n[0]}:"
        for comp in result.get("components", []):
            comp["bom-ref"] = prefix + str(comp.get("bom-ref"))
            merged["components"].append(comp)
        for vuln in result.get("vulnerabilities", []):
            for affect in vuln.get("affects", []):
                affect["ref"] = prefix + str(affect.get("ref"))
            merged["vulnerabilities"].append(vuln)

    comps = sbom.get("components", [])
    for i in range(0, len(comps), CHUNK):
        run(comps[i:i + CHUNK])
    tmp.unlink(missing_ok=True)
    return merged


def main(artifact_dir, expected_sha):
    rows, details, pr = [], [], None
    for meta in pathlib.Path(artifact_dir).glob("*/pr.json"):
        data = json.loads(meta.read_text())
        number, sha = data.get("pr"), data.get("head_sha")
        if isinstance(number, int) and number > 0 and sha == expected_sha:
            pr = number
    for path in sorted(pathlib.Path(artifact_dir).glob("*/*.cdx.json")):
        name = path.name[: -len(".cdx.json")]
        if path.stat().st_size > MAX_SBOM_BYTES:
            rows.append((name, "skipped (SBOM too large)", 0, 0))
            continue
        sbom = json.loads(path.read_text())
        if sbom.get("bomFormat") != "CycloneDX":
            rows.append((name, "skipped (not a CycloneDX SBOM)", 0, 0))
            continue
        result = scan(path)
        comps = {c.get("bom-ref"): c for c in result.get("components", [])}
        # A CVE can come back from several chunks: count unique IDs per severity.
        found = {s: {} for s in COUNTED}
        for vuln in result.get("vulnerabilities", []):
            sev = inspector_severity(vuln)
            if sev in found:
                pkgs = {comps.get(a.get("ref"), {}).get("name", "?") for a in vuln.get("affects", [])}
                found[sev].setdefault(vuln.get("id", "?"), set()).update(pkgs)
        for sev, ids in found.items():
            details += [(name, sev, vid, ", ".join(sorted(p))) for vid, p in sorted(ids.items())]
        status = "scanned"
        if result["skipped"]:
            status += f" ({len(result['skipped'])} package(s) too large to scan: {', '.join(result['skipped'])})"
        rows.append((name, status, len(found["critical"]), len(found["high"])))

    total_c = sum(r[2] for r in rows)
    total_h = sum(r[3] for r in rows)
    lines = [
        MARKER,
        "### Amazon Inspector scan of the images built by this PR",
        "",
        f"**{total_c} Critical, {total_h} High** across {len(rows)} image(s). "
        "Same engine and settings as ECR enhanced scanning.",
        "",
        "| Image | Status | Critical | High |",
        "|---|---|---|---|",
    ]
    lines += [f"| {n} | {s} | {c} | {h} |" for n, s, c, h in rows]
    crit = [d for d in details if d[1] == "critical"]
    if crit:
        lines += ["", "<details><summary>Critical findings</summary>", "",
                  "| Image | Finding | Package |", "|---|---|---|"]
        lines += [f"| {n} | {i} | {p} |" for n, _, i, p in crit]
        lines += ["", "</details>"]
    summary = "\n".join(lines) + "\n"
    pathlib.Path("summary.md").write_text(summary)
    pathlib.Path("result.json").write_text(json.dumps(
        {"pr": pr, "critical": total_c, "high": total_h, "images": len(rows)}))
    with open(os.environ.get("GITHUB_STEP_SUMMARY", os.devnull), "a") as fh:
        fh.write(summary)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
