#!/bin/sh
set -e
# You can use this to build any changes you make to Docker build images to your local machine.
# Of course, you can also run a single one of these commands manually.
# If you use this script, ensure that you run with --skip-pull-image, else the remote image may be used.

if [ -z ${SAM_CLI_VERSION+x} ];
then
    echo "Must set SAM_CLI_VERSION to run this script."
    exit -1;
else
    echo "SAM CLI VERSION: $SAM_CLI_VERSION";
fi

if [ ${SAM_CLI_CROSS_BUILD} ];
then
    CROSS_DOCKER_BUILDX="buildx"
    HOST_PLATFORM="`uname -o`/`uname -m`"
    GUEST_PLATFORM="--platform=linux/amd64"
    echo "Cross compiling of SAM CLI activated. Host is " ${HOST_PLATFORM} " with target platform flag set to: " ${GUEST_PLATFORM}
fi

docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-nodejs10x -t amazon/aws-sam-cli-build-image-nodejs10.x --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-nodejs12x -t amazon/aws-sam-cli-build-image-nodejs12.x --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-nodejs14x -t amazon/aws-sam-cli-build-image-nodejs14.x --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-java11 -t amazon/aws-sam-cli-build-image-java11 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-java8 -t amazon/aws-sam-cli-build-image-java8 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-java8-al2 -t amazon/aws-sam-cli-build-image-java8.al2 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-provided -t amazon/aws-sam-cli-build-image-provided --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-provided-al2 -t amazon/aws-sam-cli-build-image-provided.al2 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-python27 -t amazon/aws-sam-cli-build-image-python2.7 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-python36 -t amazon/aws-sam-cli-build-image-python3.6 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-python37 -t amazon/aws-sam-cli-build-image-python3.7 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-python38 -t amazon/aws-sam-cli-build-image-python3.8 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
# Disable DOCKER_CONTENT_TRUST for pulling from public ECR
DOCKER_CONTENT_TRUST=0 docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-python39 -t amazon/aws-sam-cli-build-image-python3.9 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-ruby25 -t amazon/aws-sam-cli-build-image-ruby2.5 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-ruby27 -t amazon/aws-sam-cli-build-image-ruby2.7 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
docker ${CROSS_DOCKER_BUILDX} build ${GUEST_PLATFORM} -f Dockerfile-go1x -t amazon/aws-sam-cli-build-image-go1.x --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION .
