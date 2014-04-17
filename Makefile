.PHONY: clean-pyc clean-build docs setup clean

VIRTUALENV=virtualenv
virtualenv_dir=venv

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "source - source package"

venv:
	test -d venv || ($(VIRTUALENV) $(virtualenv_dir) || true)
	. $(virtualenv_dir)/bin/activate

deps:
	pip install -r requirements/prod.txt -r requirements/dev.txt

setup: venv deps

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg*

clean-pyc:
	@echo "Clean python files: *.[pyc,pyo,__pycache__]"
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -type d -exec rm -rf {} +
	@find . -name '*~' -exec rm -f {} +

lint: venv
	@flake8 pwnurl pwnurl/tests manage.py

tox-test: venv
	@tox

test: venv
	@nosetests --with-coverage --cover-package=pwnurl

coverage: venv
	@rm -rf htmlcov
	@coverage run --source pwnurl manage.py test
	@coverage report -m
	@coverage html
	@xdg-open htmlcov/index.html

docs:
	rm -f docs/pwnurl.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pwnurl
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	@xdg-open docs/_build/html/index.html

docs-install: setup
		pip install -e '.[docs]' --use-mirrors

source: clean venv
	python setup.py sdist

release: clean venv
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean venv
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
