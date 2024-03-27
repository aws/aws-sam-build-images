# Default value for environment variable. Can be overridden by setting the
# environment variable.
export DOCKER_CONTENT_TRUST := 0
export DOCKER_CLI_EXPERIMENTAL := enabled

# image suffix lookup
IS_dotnet6 := dotnet6
IS_dotnet7 := dotnet7
IS_dotnet8 := dotnet8
IS_java8_al2 := java8.al2
IS_java11 := java11
IS_java17 := java17
IS_java21 := java21
IS_nodejs16x := nodejs16.x
IS_nodejs18x := nodejs18.x
IS_nodejs20x := nodejs20.x
IS_provided_al2 := provided.al2
IS_provided_al2023 := provided.al2023
IS_python38 := python3.8
IS_python39 := python3.9
IS_python310 := python3.10
IS_python311 := python3.11
IS_python312 := python3.12
IS_ruby32 := ruby3.2
IS_ruby33 := ruby3.3

init:
	pip install -Ur requirements.txt

build:
	cd build-image-src && ./build_all_images.sh

pre-build:
ifeq ($(strip $(SAM_CLI_VERSION)),)
	@echo "Must specify SAM_CLI_VERSION"
	exit 1
else
	@echo "SAM CLI VERSION $(SAM_CLI_VERSION)"
endif

ifeq ($(strip $(RUNTIME)),)
	@echo "Must specify RUNTIME"
	exit 1
else
	@echo "Building runtime $(RUNTIME)"
endif

build-multi-arch: pre-build
	docker build -f build-image-src/Dockerfile-$(RUNTIME) -t amazon/aws-sam-cli-build-image-$(IS_$(RUNTIME)):x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$(SAM_CLI_VERSION) --build-arg AWS_CLI_ARCH=x86_64 --build-arg GO_ARCH=amd64 --build-arg IMAGE_ARCH=x86_64 ./build-image-src
	docker run --privileged --rm tonistiigi/binfmt --install arm64
	docker build -f build-image-src/Dockerfile-$(RUNTIME) -t amazon/aws-sam-cli-build-image-$(IS_$(RUNTIME)):arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$(SAM_CLI_VERSION) --build-arg AWS_CLI_ARCH=aarch64 --build-arg GO_ARCH=arm64 --build-arg IMAGE_ARCH=arm64 ./build-image-src

build-x86_64-arch: pre-build
	docker build -f build-image-src/Dockerfile-$(RUNTIME) -t amazon/aws-sam-cli-build-image-$(IS_$(RUNTIME)):x86_64 --platform linux/amd64 --build-arg SAM_CLI_VERSION=$(SAM_CLI_VERSION) --build-arg AWS_CLI_ARCH=x86_64 --build-arg GO_ARCH=amd64 --build-arg IMAGE_ARCH=x86_64 ./build-image-src

build-arm64-arch: pre-build
	docker build -f build-image-src/Dockerfile-$(RUNTIME) -t amazon/aws-sam-cli-build-image-$(IS_$(RUNTIME)):arm64 --platform linux/arm64 --build-arg SAM_CLI_VERSION=$(SAM_CLI_VERSION) --build-arg AWS_CLI_ARCH=aarch64 --build-arg GO_ARCH=arm64 --build-arg IMAGE_ARCH=arm64 ./build-image-src

test: pre-build
	pytest tests -vv -m "$(RUNTIME)$(ARCH)"

lint:
	# Linter performs static analysis to catch latent bugs
	pylint --rcfile .pylintrc tests
	# mypy performs type check
	mypy tests/*.py

dev: lint test

black:
	black tests

black-check:
	black --check tests

# Verifications to run before sending a pull request
pr: init build black-check dev
