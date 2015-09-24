.PHONY: clean install test

DEFAULT_APP=project

help:
	@echo "clean - remove test artifacts"
	@echo "install - install python dependencies"
	@echo "test - run test"

clean:
	rm -fr $(DEFAULT_APP)

install: clean
	pip install cookiecutter

build: clean
	cookiecutter --no-input .
	cd $(DEFAULT_APP) && make install

test: build
	cd $(DEFAULT_APP) && make test
