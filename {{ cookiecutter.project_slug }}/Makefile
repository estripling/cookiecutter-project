SHELL := /bin/bash
PYTHON := python
POETRY := poetry

.PHONY: help \
	start \
	install \
	check \
	check-style \
	run-tests \
	clean \
	remove-local-branches

## commands
##  - help                                 :: print this help
help: Makefile
	@sed -n 's/^##//p' $<

##  - start                                :: start JupyterLab in Docker container
start:
	@docker compose up --build

##  - install                              :: install dependencies with Poetry
install:
	$(POETRY) install

##  - check                                :: check style, run tests, and clean up cache all at once
check: clean check-style run-tests clean

##  - check-style                          :: check code style with isort, black, and flake8
check-style:
	$(PYTHON) -m isort ./
	@echo ''
	$(PYTHON) -m black ./
	@echo ''
	$(PYTHON) -m flake8 ./
	@echo ''

##  - run-tests                            :: run pytest with coverage report
run-tests:
	$(PYTHON) -m pytest
	@echo ''

##  - clean                                :: remove Python cache files and directories
clean:
	$(PYTHON) scripts/cleanup.py
	@echo ''

##  - remove-local-branches                :: git remove local branches, except main
remove-local-branches:
	git -P branch | grep -v "main" | grep -v \* | xargs git branch -D
