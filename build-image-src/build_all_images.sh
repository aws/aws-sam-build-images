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

# Disable DOCKER_CONTENT_TRUST for pulling from public ECR
export DOCKER_CONTENT_TRUST=0
export DOCKER_CLI_EXPERIMENTAL=enabled

# Single arch images
docker build -f Dockerfile-java8 -t amazon/aws-sam-cli-build-image-java8:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-nodejs10x -t amazon/aws-sam-cli-build-image-nodejs10.x:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-provided -t amazon/aws-sam-cli-build-image-provided:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-python27 -t amazon/aws-sam-cli-build-image-python2.7:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-python36 -t amazon/aws-sam-cli-build-image-python3.6:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-python37 -t amazon/aws-sam-cli-build-image-python3.7:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-ruby25 -t amazon/aws-sam-cli-build-image-ruby2.5:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
docker build -f Dockerfile-go1x -t amazon/aws-sam-cli-build-image-go1.x:x86_64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION . &
wait

# Multi arch images
# First build all x86
docker build -f Dockerfile-dotnetcore31 -t amazon/aws-sam-cli-build-image-dotnetcore3.1:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java8-al2 -t amazon/aws-sam-cli-build-image-java8.al2:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java11 -t amazon/aws-sam-cli-build-image-java11:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-nodejs12x -t amazon/aws-sam-cli-build-image-nodejs12.x:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-nodejs14x -t amazon/aws-sam-cli-build-image-nodejs14.x:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-provided-al2 -t amazon/aws-sam-cli-build-image-provided.al2:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python38 -t amazon/aws-sam-cli-build-image-python3.8:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python39 -t amazon/aws-sam-cli-build-image-python3.9:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-ruby27 -t amazon/aws-sam-cli-build-image-ruby2.7:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
wait

# Delete multi arch al2 image and start building arm64 images
docker rmi public.ecr.aws/amazonlinux/amazonlinux:2
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker build -f Dockerfile-dotnetcore31 -t amazon/aws-sam-cli-build-image-dotnetcore3.1:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java8-al2 -t amazon/aws-sam-cli-build-image-java8.al2:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java11 -t amazon/aws-sam-cli-build-image-java11:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-nodejs12x -t amazon/aws-sam-cli-build-image-nodejs12.x:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-nodejs14x -t amazon/aws-sam-cli-build-image-nodejs14.x:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-provided-al2 -t amazon/aws-sam-cli-build-image-provided.al2:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python38 -t amazon/aws-sam-cli-build-image-python3.8:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python39 -t amazon/aws-sam-cli-build-image-python3.9:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-ruby27 -t amazon/aws-sam-cli-build-image-ruby2.7:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
wait
