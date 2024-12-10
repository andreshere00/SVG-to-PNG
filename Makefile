# Variables
DOCKER = sudo docker
PIPENV = pipenv run
PEP8 = autopep8
IMAGE_NAME = svg-to-png
ENV_FILE = .env

# Targets
.PHONY: serve build run d-build d-run autopep8 pre-commit help

help:
	@echo "Available commands:"
	@echo "  make serve       - Build and start services using docker-compose."
	@echo "  make build       - Build Docker images using docker-compose."
	@echo "  make run         - Start containers using docker-compose."
	@echo "  make prune       - Remove all stopped containers."
	@echo "  make autopep8    - Format code with autopep8."
	@echo "  make pre-commit  - Install and run pre-commit hooks on all files."

serve:
	$(DOCKER) container prune --force
	$(DOCKER) compose up --build

build:
	$(DOCKER) compose build

run:
	$(DOCKER) compose up

d-build:
	$(DOCKER) build -t $(IMAGE_NAME) .

d-run:
	$(DOCKER) run --env-file $(ENV_FILE) $(IMAGE_NAME)

autopep8:
	$(PIPENV) $(PEP8) --in-place --recursive .

pre-commit:
	$(PIPENV) install --dev
	$(PIPENV) run pre-commit install
	$(PIPENV) run pre-commit run --all-files
