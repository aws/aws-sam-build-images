#!/usr/bin/env python3
"""Decide which build images to build, based on the Lambda runtime lifecycle.

lambda_runtimes.json (next to this file) has:
  last_updated  date the data was last checked against the sources (YYYY-MM-DD);
                bump it whenever you re-check, even if nothing changed
  sources       the Lambda documentation pages the data comes from
  runtimes      every Lambda runtime, supported and deprecated, keyed by
                runtime identifier, with:
  dockerfile             suffix of build-image-src/Dockerfile-<suffix>, or null
                         if this repo has no build image for the runtime
  os                     Amazon Linux version the runtime is based on
  deprecation            Lambda deprecation date (YYYY-MM-DD)
  block_function_create  date Lambda blocks function creation, or null
  block_function_update  date Lambda blocks function updates, or null
  note                   optional, e.g. "container only"

`validate` warns when last_updated is more than STALE_AFTER_DAYS old.

A runtime is skipped by `make build-*`, `build_all_images.sh` and the GitHub
Actions build matrix once its deprecation date is today or earlier (UTC), so
supported runtimes stop building on their published date with no code change.
Dockerfiles and tests stay in the repo; set ALLOW_DEPRECATED=1 to build a
deprecated runtime anyway (for example to ship an urgent fix). Images that
were already published stay available in Amazon ECR Public.

Usage:
  deprecated_runtimes.py is-deprecated <runtime-or-dockerfile-suffix> [--date YYYY-MM-DD]
      exit 0 and print the reason if deprecated, exit 1 otherwise
  deprecated_runtimes.py supported
      JSON list of Dockerfile suffixes that are not deprecated
  deprecated_runtimes.py validate
      fail if a Dockerfile has no entry, or an entry names a missing Dockerfile;
      warn if last_updated is stale
"""

import argparse
import datetime
import json
import pathlib
import sys
from typing import NamedTuple, Optional


class Runtime(NamedTuple):
    identifier: str
    dockerfile: Optional[str]
    os: str
    deprecation: datetime.date
    block_function_create: Optional[datetime.date]
    block_function_update: Optional[datetime.date]
    note: Optional[str]


BUILD_IMAGE_SRC = pathlib.Path(__file__).resolve().parent
DATA_FILE = BUILD_IMAGE_SRC / "lambda_runtimes.json"
STALE_AFTER_DAYS = 90


def _date(value: Optional[str]) -> Optional[datetime.date]:
    return datetime.date.fromisoformat(value) if value else None


def load(path: pathlib.Path = DATA_FILE) -> tuple:
    """(last_updated, {Lambda runtime identifier -> Runtime}) from lambda_runtimes.json."""
    data = json.loads(path.read_text())
    return datetime.date.fromisoformat(data["last_updated"]), {
        identifier: Runtime(
            identifier=identifier,
            dockerfile=entry.get("dockerfile"),
            os=entry["os"],
            deprecation=datetime.date.fromisoformat(entry["deprecation"]),
            block_function_create=_date(entry.get("block_function_create")),
            block_function_update=_date(entry.get("block_function_update")),
            note=entry.get("note"),
        )
        for identifier, entry in data["runtimes"].items()
    }


LAST_UPDATED, RUNTIMES = load()


def today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def lookup(name: str) -> Optional[Runtime]:
    """Find a runtime by Lambda identifier (python3.8) or Dockerfile suffix (python38)."""
    if name in RUNTIMES:
        return RUNTIMES[name]
    return next((r for r in RUNTIMES.values() if r.dockerfile == name), None)


def is_deprecated(name: str, on: Optional[datetime.date] = None) -> bool:
    runtime = lookup(name)
    return runtime is not None and runtime.deprecation <= (on or today())


def dockerfiles() -> list:
    return sorted(p.name[len("Dockerfile-"):] for p in BUILD_IMAGE_SRC.glob("Dockerfile-*"))


def supported_dockerfiles(on: Optional[datetime.date] = None) -> list:
    return [d for d in dockerfiles() if not is_deprecated(d, on)]


def validate() -> list:
    errors = []
    known = {r.dockerfile for r in RUNTIMES.values() if r.dockerfile}
    for d in dockerfiles():
        if d not in known:
            errors.append(f"build-image-src/Dockerfile-{d} has no entry in lambda_runtimes.json")
    for r in RUNTIMES.values():
        if r.dockerfile and not (BUILD_IMAGE_SRC / f"Dockerfile-{r.dockerfile}").is_file():
            errors.append(f"lambda_runtimes.json: {r.identifier} names missing build-image-src/Dockerfile-{r.dockerfile}")
    return errors


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("is-deprecated")
    check.add_argument("runtime")
    check.add_argument("--date", type=datetime.date.fromisoformat)
    sub.add_parser("supported")
    sub.add_parser("validate")
    args = parser.parse_args(argv)

    if args.command == "is-deprecated":
        if not is_deprecated(args.runtime, args.date):
            return 1
        runtime = lookup(args.runtime)
        print(f"{runtime.identifier} is deprecated ({runtime.deprecation}); see build-image-src/lambda_runtimes.json")
        return 0
    if args.command == "supported":
        print(json.dumps(supported_dockerfiles()))
        return 0
    errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    age = (today() - LAST_UPDATED).days
    if age > STALE_AFTER_DAYS:
        # "::warning::" renders as an annotation in GitHub Actions; plain text elsewhere.
        print(f"::warning::lambda_runtimes.json was last updated {LAST_UPDATED} ({age} days ago); "
              "re-check it against the Lambda runtime docs and bump last_updated", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
