#!/bin/sh
set -e
# You can use this to build any changes you make to Docker build images to your local machine.
# Of course, you can also run a single one of these commands manually.
# If you use this script, ensure that you run with --skip-pull-image, else the remote image may be used.

if [ -z ${SAM_CLI_VERSION+x} ];
then
    echo "Must set SAM_CLI_VERSION to run this script."
    exit 1;
else
    echo "SAM CLI VERSION: $SAM_CLI_VERSION";
fi

# Disable DOCKER_CONTENT_TRUST for pulling from public ECR
export DOCKER_CONTENT_TRUST=0
export DOCKER_CLI_EXPERIMENTAL=enabled


# Multi arch images
# First build all x86
docker build -f Dockerfile-dotnet6 -t amazon/aws-sam-cli-build-image-dotnet6:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-dotnet7 -t amazon/aws-sam-cli-build-image-dotnet7:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-dotnet8 -t amazon/aws-sam-cli-build-image-dotnet8:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java8_al2 -t amazon/aws-sam-cli-build-image-java8.al2:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java11 -t amazon/aws-sam-cli-build-image-java11:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java17 -t amazon/aws-sam-cli-build-image-java17:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-java21 -t amazon/aws-sam-cli-build-image-java21:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-nodejs16x -t amazon/aws-sam-cli-build-image-nodejs16.x:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-nodejs18x -t amazon/aws-sam-cli-build-image-nodejs18.x:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-nodejs20x -t amazon/aws-sam-cli-build-image-nodejs20.x:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-provided_al2 -t amazon/aws-sam-cli-build-image-provided.al2:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg GO_ARCH=amd64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-provided_al2023 -t amazon/aws-sam-cli-build-image-provided.al2023:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python38 -t amazon/aws-sam-cli-build-image-python3.8:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python39 -t amazon/aws-sam-cli-build-image-python3.9:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python310 -t amazon/aws-sam-cli-build-image-python3.10:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python311 -t amazon/aws-sam-cli-build-image-python3.11:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-python312 -t amazon/aws-sam-cli-build-image-python3.12:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-ruby32 -t amazon/aws-sam-cli-build-image-ruby3.2:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
docker build -f Dockerfile-ruby33 -t amazon/aws-sam-cli-build-image-ruby3.3:x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=x86_64 --build-arg IMAGE_ARCH=x86_64 . &
wait

# Build arm64 images
docker run --privileged --rm tonistiigi/binfmt --install arm64
docker build -f Dockerfile-dotnet6 -t amazon/aws-sam-cli-build-image-dotnet6:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-dotnet7 -t amazon/aws-sam-cli-build-image-dotnet7:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-dotnet8 -t amazon/aws-sam-cli-build-image-dotnet8:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java8_al2 -t amazon/aws-sam-cli-build-image-java8.al2:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java11 -t amazon/aws-sam-cli-build-image-java11:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java17 -t amazon/aws-sam-cli-build-image-java17:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-java21 -t amazon/aws-sam-cli-build-image-java21:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-nodejs16x -t amazon/aws-sam-cli-build-image-nodejs16.x:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-nodejs18x -t amazon/aws-sam-cli-build-image-nodejs18.x:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-nodejs20x -t amazon/aws-sam-cli-build-image-nodejs20.x:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-provided_al2 -t amazon/aws-sam-cli-build-image-provided.al2:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg GO_ARCH=arm64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-provided_al2023 -t amazon/aws-sam-cli-build-image-provided.al2023:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python38 -t amazon/aws-sam-cli-build-image-python3.8:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python39 -t amazon/aws-sam-cli-build-image-python3.9:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python310 -t amazon/aws-sam-cli-build-image-python3.10:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python311 -t amazon/aws-sam-cli-build-image-python3.11:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-python312 -t amazon/aws-sam-cli-build-image-python3.12:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-ruby32 -t amazon/aws-sam-cli-build-image-ruby3.2:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
docker build -f Dockerfile-ruby33 -t amazon/aws-sam-cli-build-image-ruby3.3:arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$SAM_CLI_VERSION --build-arg AWS_CLI_ARCH=aarch64 --build-arg IMAGE_ARCH=arm64 . &
wait
