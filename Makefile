.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard nbs/*.ipynb)

all: test_nbdev docs

test_nbdev: $(SRC)
	nbdev_build_lib
	touch test_nbdev

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi conda_release
	nbdev_bump_version

conda_release:
	fastrelease_conda_package

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

downgrade-nbconvert:
	pip install nbconvert==5.6.1

install-twine:
	pip install twine

setup: downgrade-nbconvert install-twine
	nbdev_install_git_hooks