define PRINT_HELP_PYSCRIPT
import re, sys

print(r"""
make targets for managing the project virtual environment on Unix systems:
""")
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.venv/bin/python:
	conda env create -p ./.venv -f environment.yml

venv: ./.venv/bin/python  ## create the local project environment

install: .venv/bin/python ## install project kernel globally
	$< -m ipykernel install --user --name jupyter-tutorial-rydberg --display-name "Jupyter Tutorial (Rydberg)"

uninstall: ## remove globally installed project kernel
	jupyter kernelspec remove -f jupyter-tutorial-rydberg || true

clean: ## remove files produced by executing notebooks
	rm -rf prop.dump
	rm -rf .ipynb_checkpoints

dist-clean: clean uninstall ## Restore checkout to a pristine state, removing the local project environment
	rm -rf .venv

.PHONY: help venv install uninstall clean dist-clean
