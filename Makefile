# Default value for environment variable. Can be overridden by setting the
# environment variable.

init:
	SAM_CLI_DEV=1 pip install -e '.[dev]'

build:
	build-image-src/build_all_images.sh

test:
	pytest tests

dev:
	lint test

black:
	black setup.py tests

black-check:
	black --check setup.py tests

# Verifications to run before sending a pull request
pr: init build black-check dev