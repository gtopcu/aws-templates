
CURRENT_DIR := $(shell pwd)
# CURRENT_DIR := $(CURDIR)

.PHONY: help show-dir init deps update build scan check lint test clean deploy
# env-create env-activate install-dev install

# Default target when just running 'make'
help:
	@echo "Available commands:"
#	@echo "make env-create   - Create virtual environment"
#	@echo "make env-activate - Activate virtual environment"
	@echo "make init         - Initializes poetry and installs dependencies"
	@echo "make deps         - Create requirements.txt files"
#	@echo "make install-dev  - Install dev dependencies"
#	@echo "make install      - Install dependencies"
	@echo "make update       - Update dependencies"
	@echo "make build        - Build package"
	@echo "make scan         - Run vulnerability scanner"
	@echo "make check        - Run pre-commit on all files"
	@echo "make lint         - Run linters"
	@echo "make test         - Run tests"
	@echo "make clean        - Clean up cache files"
	@echo "make deploy       - Deploy to AWS"

show-dir:
	@echo "Current working directory: $(CURRENT_DIR)"
#	@echo "Using pwd command: $(shell pwd)"

# env-create:
#	python -m venv $(CURRENT_DIR)/.venv

# env-activate:
#	source $(CURRENT_DIR)/.venv/bin/activate
#	poetry shell

init:
#	curl -sSL https://install.python-poetry.org | python3 -
#	pip install --upgrade poetry poetry-plugin-export
	poetry --version
	poetry config virtualenvs.in-project true
	poetry install --sync
	poetry shell

deps:
	poetry export -v --with dev --without-hashes -o requirements-dev.txt
	poetry export -v --without-hashes -o requirements.txt

# install-dev:
#	pip install -r requirements-dev.txt
#	pre-commit install

# install:
#	pip install -r requirements.txt
#	pre-commit install

update:
	poetry update -v

build:
	poetry build -v

scan:
	safety scan --detailed-output --apply-fixes

check:
	pre-commit run --all-files -v

lint:
	isort .
	ruff check --fix
	ruff format
	pylint .
	pyright .

test:
	pytest -vs --cov

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
# 	rm -rf $(CURRENT_DIR)/build/*
#	rm -rf cdk.out

deploy:
	cdk deploy --all
