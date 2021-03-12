# Default value for environment variable. Can be overridden by setting the
# environment variable.

init:
	pip install -Ur requirements.txt

build:
	build-image-src/build_all_images.sh

test:
	pytest tests

lint:
	# Linter performs static analysis to catch latent bugs
	pylint --rcfile .pylintrc tests
	# mypy performs type check
	mypy tests

dev:
	lint test

black:
	black tests

black-check:
	black --check tests

# Verifications to run before sending a pull request
pr: init build black-check dev