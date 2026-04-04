# Auto-document targets with "## description"
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

# Project setup
PYTHONPATH=src

setup-db: ## Runs db setup script.
	PYTHONPATH=$(PYTHONPATH) python -m db.scripts.setup

run: ## Runs project in ./src/app/api.py
	PYTHONPATH=$(PYTHONPATH) python -m app.api