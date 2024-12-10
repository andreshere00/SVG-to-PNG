# Variables
DOCKER = sudo docker
PIPENV = pipenv run
PEP8 = autopep8
IMAGE_NAME = svg-to-png
ENV_FILE = .env
CHANGELOG_FILE = CHANGELOG.md

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
	# Generate a changelog and insert it at the marker
	TMP_CHANGELOG=$$(mktemp); \
	$(PIPENV) git log --pretty=format:"- %s ([%h](https://github.com/andreshere00/SVG-to-PNG/commit/%h)) by %an on %ad" --date=short > $$TMP_CHANGELOG; \
	awk -v new_changelog=$$TMP_CHANGELOG '1; /<!-- insertion marker -->/ { while(getline line < new_changelog) print line; }' $(CHANGELOG_FILE) > $(CHANGELOG_FILE).new; \
	mv $(CHANGELOG_FILE).new $(CHANGELOG_FILE); \
	rm $$TMP_CHANGELOG; \
	echo "Changelog updated successfully!"

release:
	# Create a new release
	@echo "Enter the new version (e.g., v1.0.0): "
	@read version; \
	echo "Releasing $$version..."; \
	git tag $$version; \
	git push origin $$version; \
	echo "Updating changelog..."; \
	make changelog; \
	git add $(CHANGELOG_FILE); \
	git commit -m "Update changelog for $$version"; \
	git push origin main; \
	echo "Release $$version completed."
