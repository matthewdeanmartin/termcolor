.DEFAULT_GOAL := help
UV := uv
RUN := $(UV) run --frozen --python 3.14

.PHONY: help sync test docs build dist-check artifact-check changelog-check check

help:
	@echo "sync test docs build dist-check artifact-check changelog-check check"

sync:
	$(UV) sync --no-build --frozen --python 3.14

test:
	$(RUN) pytest -q test termcolor --doctest-modules

docs:
	$(UV) tool run --no-build --python 3.14 --with-requirements docs/requirements.txt mkdocs build --strict

build:
	$(UV) build --no-sources
	@"$(MAKE)" dist-check
	@"$(MAKE)" artifact-check

dist-check:
	$(UV) tool run --no-build --python 3.14 --from 'twine>=7' twine check --strict dist/*
	$(UV) tool run --no-build --python 3.14 --from 'check-wheel-contents>=0.6' check-wheel-contents dist/*.whl

artifact-check:
	$(RUN) python -X utf8 scripts/check_installed_distribution.py $$(python -X utf8 -c "import tomllib; print(tomllib.load(open('pyproject.toml','rb'))['project']['version'])")

changelog-check:
	$(UV) tool run --no-build --python 3.14 --from keepachangelog-manager-fork kaclm validate

check: test docs changelog-check build
