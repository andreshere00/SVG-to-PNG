# Variables
DOCKER = sudo docker
PIPENV = pipenv run
PEP8 = autopep8
IMAGE_NAME = svg-to-png
ENV_FILE = .env

# Targets
.PHONY: serve build run prune autopep8 pre-commit changelog release help

help:
	@echo "Available commands:"
	@echo "  make serve       - Build and start services using docker-compose."
	@echo "  make build       - Build Docker images using docker-compose."
	@echo "  make run         - Start containers using docker-compose."
	@echo "  make prune       - Remove all stopped containers."
	@echo "  make autopep8    - Format code with autopep8."
	@echo "  make pre-commit  - Install and run pre-commit hooks on all files."
	@echo "  make changelog   - Generate a basic changelog."
	@echo "  make release     - Create a new release (update version and changelog)."

serve:
	cp .env.template .env
	$(DOCKER) compose up --build

build:
	$(DOCKER) compose build

run:
	$(DOCKER) compose up

prune:
	$(DOCKER) container prune --force

autopep8:
	$(PIPENV) $(PEP8) --in-place --recursive .

pre-commit:
	pipenv install --dev
	$(PIPENV) pre-commit install
	$(PIPENV) pre-commit autoupdate
	$(PIPENV) pre-commit run --all-files

changelog:
	# Generate a basic changelog with git-changelog and git log
	$(PIPENV) git-changelog > CHANGELOG.md
	$(PIPENV) git log --pretty=format:"- %s (%h)" >> CHANGELOG.md
	$(PIPENV) git log --pretty=format:"- %s (%h) by %an on %ad" --date=short >> CHANGELOG.md

release:
	# Create a new version
	@echo "Enter the new version (e.g., v1.0.0): "
	@read version; \
	echo "Releasing $$version..."; \
	git tag $$version; \
	git push origin $$version; \
	echo "Generating changelog..."; \
	$(PIPENV) git-changelog > CHANGELOG.md; \
	$(PIPENV) git log --pretty=format:"- %s (%h)" >> CHANGELOG.md; \
	$(PIPENV) git log --pretty=format:"- %s (%h) by %an on %ad" --date=short >> CHANGELOG.md; \
	git add CHANGELOG.md; \
	git commit -m "Update changelog for $$version"; \
	git push origin main; \
	echo "Release $$version completed."
