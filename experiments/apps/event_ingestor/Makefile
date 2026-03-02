.PHONY: lock sync lint format mypy unit integration

VENV := .venv
ENV_RUNNER ?= uv
SRC := src
DOC ?= document_1.txt

wait:
	sleep 5


sync-git-workspace:
	cd ../../../ && make sync-experiments


sync-uv-workspace:
	cd ../../../ && make sync 



# =========================
# 		Code Quality
# =========================
quality: format lint mypy
quality-ruff: format lint

lint:
	@$(ENV_RUNNER) run ruff check . --fix
lint-check:
	@$(ENV_RUNNER) run ruff check .

format:
	@$(ENV_RUNNER) run ruff format .
format-check:
	@$(ENV_RUNNER) run ruff format . --check

mypy:
	@$(ENV_RUNNER) run mypy .



# --------------------------
# Tests
# --------------------------
tests: test-unit test-integration
tests-integration:
	@uv run pytest --cov --cov-report=term-missing --cov-report=html tests

test-unit:
	@uv run pytest -m unit tests/unit
test-unit-coverage:
	@uv run pytest -m unit --cov --cov-report=term-missing --cov-report=html tests/unit

test-integration:
	@uv run pytest -m integration tests/integration
test-integration-coverage:
	@uv run pytest -m integration --cov --cov-report=term-missing --cov-report=html tests/integration
	
# --------------------------
# Scripts
# --------------------------

