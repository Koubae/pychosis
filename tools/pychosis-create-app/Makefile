.PHONY: lock sync lint format mypy unit integration

sync:
	git pull; git status; git add .; git commit -a -m "Sync changes"; git push; printf "\n\n🔎 Checking Sync Status.... 🪄\n"; git status;

sync-experiments:
	git pull; git status; git add ./experiments; git commit -a -m "Sync Experiment 🧪 changes"; git push; printf "\n\n🔎 Checking Sync Status (Experiment 🧪).... 🪄\n"; git status;


VENV := .venv
ENV_RUNNER ?= uv
SRC := src
DOC ?= document_1.txt

wait:
	sleep 5

# ============================
#       RUN
# ============================

# --------------------------
# Docker
# --------------------------

# --------------------------
# Run (no-docker)
# --------------------------
# ////////////////////
#	App ,.,,
# ////////////////////

# ////////////////

# --------------------------
# Init
# --------------------------
init-venv: update-env-file .install-uv .create-venv update-venv install-deps
update-venv: lock sync

lock:
	@uv lock
sync:
	@uv sync --dev

.install-uv:
	pip install -U uv

.create-venv:
	@if [ -d "./.venv" ]; then \
		echo ".venv python environment exists, skipping..."; \
	else \
		echo ".venv not found, Creating Python environment..."; \
		UV_VENV_CLEAR=1 uv venv; \
	fi

install-deps:
	@uv pip install -e . --group dev

update-env-file:
	@echo 'Updating .env from .env.example 🖋️...'
	@cp .env.example .env
	@echo '.env Updated ✨'


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

# --------------------------
# Scripts
# --------------------------
