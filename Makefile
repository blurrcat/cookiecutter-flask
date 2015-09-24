.PHONY: clean install test

help:
	@echo "clean - remove test artifacts"
	@echo "install - install python dependencies"
	@echo "test - run test"

clean:
	rm -fr forest_owlet

install: clean
	pip install cookiecutter

test: clean
	cookiecutter --no-input .
	cd forest_owlet && make install && make test
