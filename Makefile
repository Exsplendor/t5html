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
EMAIL := <em.notorp@sirolf.rodnelps>
VERSION := $(shell date +%y.%m.%d)
DESC := "Converts text to html. Text muste be in t5html form."
CVSURL := ""
TOPIC := "Topic :: Text Processing :: Markup :: HTML"

define HELP

## ${TITLE} Makefile ##

There's no default target.

Usage:
    make
    make init
        create initial projecct structure
    make help

endef

define SETUPCFG
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = ${TITLE}
version = ${VERSION}
authors = [
  { name=${AUTHOR}, email=${EMAIL} },
]
description = "${DESC}"
readme = "Read.Me"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 1 - Planning",
    ${TOPIC},
]

[project.urls]
"Homepage" = "${CVSURL}"
"Bug Tracker" = "${CVSURL}/issues"

endef


PYTHON := python3

VENV := venv
VENVDIR := meta/${VENV}
VENVSTART := ${VENVDIR}/bin/activate

CVS := git
CVS_IGNORE := .${CVS}ignore


## ..................................................................... Targets

.PHONY: init clean install uninstall help

help: export _HELP_TEXT:=$(HELP)
help:
> @echo "$${_HELP_TEXT}"


init: initdirs initvenv init${CVS}
> @echo "Done ($@)"

.PHONY:
initdirs:
> @mkdir -p ./{doc,src,test,meta/script}

.PHONY:
initvenv:
> @${PYTHON} -m ${VENV} ${VENVDIR}
> @echo "Activate your virtual-environment by sourcing: source ${VENVSTART}"
> @echo "Done ($@)."

.PHONY:
initgit: ${CVS_IGNORE}
> @echo "Done ($@)."

${CVS_IGNORE}:
> @echo -e "*.swp\n*.pyc\n\n${VENVDIR}\n\n.tox\n.pytest_cache\n" >> $@
> @echo "Done ($@)."


clean:
> @echo "TARGET UNIMPLEMENTED"


install:
> @echo "TARGET UNIMPLEMENTED"


uninstall:
> @echo "TARGET UNIMPLEMENTED"


# vi: et sw=4 ts=4 list
