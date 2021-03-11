#!/usr/bin/env python

import io
import os
from setuptools import setup


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    # io.open defaults to \n as universal line ending no matter on what system
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_requirements(req="base.txt"):
    content = read(os.path.join("requirements", req))
    requirements = list()
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("#"):
            continue
        elif line.startswith("-r"):
            requirements.extend(read_requirements(line[3:]))
        else:
            requirements.append(line)
    return requirements


setup(
    name="aws-sam-build-images",
    description="AWS SAM Build Images contains docker images for all supported runtimes to build and deploy serverless applications",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Amazon Web Services",
    author_email="aws-sam-developers@amazon.com",
    url="https://github.com/aws/aws-sam-build-images",
    license="Apache License 2.0",
    keywords="AWS SAM Build Images",
    # Support Python 3.6 or greater
    python_requires=">=3.6, <=4.0, !=4.0",
    install_requires=read_requirements("base.txt"),
    extras_require={"dev": read_requirements("dev.txt")},
)
