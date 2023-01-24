#!/usr/bin/bash
# project : t5html
# date    : 01/18/23
# author  : splendor <em.notorp@sirolf.rodnelps>
# desc    : creates html from t5html-formated text files
# license : MIT License


## Makfefile-Defaults

SHELL := bash
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.SHELLFLAGS := -o errexit -o nounset -o pipefail -c
.ONESHELL:
.RECIPEPREFIX = >
.DELETE_ON_ERROR:


## ............................................................ Project Defaults

TITLE := t5html
AUTHOR := splendor
EMAIL := em.notorp@sirolf.rodnelps
VERSION := $(shell date +%y.%m.%d)
DESC := "Converts text to html. Text muste be in t5html form."
CVSURL := ""
TOPIC := "Topic :: Text Processing :: Markup :: HTML"
CFGFILE := pyproject.toml

define HELP

## ${TITLE} Makefile ##

Usage:

    make
        shows this help, same as 'make help'

    make init
        create initial projecct structure

    make initvenv
        (re)create virtualenv

    make build
        calls the build-frontend, e.g.: `python -m build`

    make dist-clean
        removes the build-directory (normally: dist)

    make publish
        uploads the build into pypi (test-pypi atm)

endef

define PYPROJECT_TOML
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "${TITLE}"
version = "${VERSION}"
authors = [
  { name="${AUTHOR}", email="${EMAIL}" },
]
description = ${DESC}
readme = "doc/ReadMe.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 1 - Planning",
    ${TOPIC},
]

[project.urls]
#"Homepage" = ${CVSURL}
#"Bug Tracker" = ${CVSURL}/issues


[tool.pytest.ini_options]
pythonpath = [ "src", ]
endef


## ........................................................... Build Environment

PYTHON := python3

VENV := venv
VENVDIR := meta/${VENV}
VENVSTART := ${VENVDIR}/bin/activate

CVS := git
CVS_IGNORE := .${CVS}ignore


## ..................................................................... Targets


help: export _HELP_TEXT:=$(HELP)
help:
> @echo "$${_HELP_TEXT}"


init: initdirs initvenv init${CVS}
> @echo "Done ($@)"

initdirs:
> @mkdir -p ./{doc,src,test,meta/script}

initvenv:
> @${PYTHON} -m ${VENV} ${VENVDIR}
> @echo "Activate your virtual-environment by sourcing: source ${VENVSTART}"

initgit: ${CVS_IGNORE}

${CVS_IGNORE}:
> @echo -e "*.swp\n*.pyc\n\n${VENVDIR}\n\n.tox\n.pytest_cache\n" >> $@

build: initbuild
> pip -V | grep ${VENV} || source ${VENVSTART}
> ${PYTHON} -m build

initbuild: ${CFGFILE}
> pip -V | grep ${VENV} || source ${VENVSTART}
> pip install --require-virtualenv build

pyproject.toml: export _CFGFILE:=${PYPROJECT_TOML}
pyproject.toml:
> @echo "$${_CFGFILE}" > $@


dist-clean:
> @rm -rf dist .pytest_cache


version-bump:
> sed -i "s/version = .*/version = ${VERSION}/" ${CFGFILE}


publish: build
> twine upload --repository testpypi dist/t5html*


# vi: et sw=4 ts=4 list
