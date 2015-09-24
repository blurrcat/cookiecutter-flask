.PHONY: clean-pyc clean-build install test coverage testing

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "install - install python dependencies"
	@echo "run - run server in debug mode"
	@echo "test - run tests with coverage"
	@echo "coverage - report coverage"
	@echo "testing - watch file changes and constantly run tests"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr pytest.xml
	rm -fr htmlcov

clean-pyc:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

install: clean
	pip install -e .[dev]

run:
	./manage.py runserver -p 5050 --debug

test: clean
	coverage run --branch --source {{cookiecutter.app}} -m py.test tests --junitxml=.pytest.xml
	@coverage html
	@echo "open htmlcov/index.html for coverage report"

coverage:
	@coverage report

testing: clean
	py.test -f
