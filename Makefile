# Default value for environment variable. Can be overridden by setting the
# environment variable.
export DOCKER_CONTENT_TRUST := 0
export DOCKER_CLI_EXPERIMENTAL := enabled

init:
	pip install -Ur requirements.txt

build:
	cd build-image-src && ./build_all_images.sh

pre-build:
	ifeq ($(SAM_CLI_VERSION),)
		exit 1
	else
		echo "SAM CLI VERSION $(SAM_CLI_VERSION)"
	endif

	ifeq ($(runtime),)
		exit 1
	else
		echo "Building runtime $(runtime)"
	endif

build-single-arch: pre-build
	cd build-image-src
	docker build -f Dockerfile-$(runtime) -t amazon/aws-sam-cli-build-image-$(runtime):x86_64 --build-arg SAM_CLI_VERSION=$(SAM_CLI_VERSION) .

test:
	pytest tests

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
