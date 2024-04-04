# Use bash syntax
# Ref:https://askubuntu.com/questions/95365/
SHELL := /bin/bash
-include .env
export $(shell sed 's/=.*//' .env)

DOCKER_DEFAULT_PLATFORM ?= linux/amd64

.EXPORT_ALL_VARIABLES:

.ONESHELL:

.phony:
	help

## ============================================================================
## Help Commands

help: ## Show help
	sed -ne '/sed/!s/## //p' $(MAKEFILE_LIST)

gen-env: ## Generate .env file
	$(call FUNC_MAKE_INIT) \
	&& cp .env.sample .env \
	&& sed -i 's,DJ_SECRET_KEY=,DJ_SECRET_KEY='"$(shell LC_ALL=C \
	tr -dc 'A-Za-z0-9' </dev/urandom \
	| head -c 120; echo \
	)"',' .env

## ============================================================================
## docker Commands

build: ## build container image via docker
	$(call FUNC_MAKE_INIT) \
	&& docker build \
	--file container/Dockerfile \
	--tag ghcr.io/yellowsoar/mav:latest \
	--tag ghcr.io/yellowsoar/musical_activity_viewer:latest \
	.

up: ## run container
	$(call FUNC_MAKE_INIT) \
	&& docker compose \
	-f container/docker-compose.yml \
	up \
	--detach

log: ## get container log
	$(call FUNC_MAKE_INIT) \
	&& docker compose \
	-f container/docker-compose.yml \
	logs \
	--follow \
	--tail 20

rm: ## rm container
	$(call FUNC_MAKE_INIT) \
	&& docker compose \
	-f container/docker-compose.yml \
	rm \
	--stop \
	--force

shell: ## container instance tty
	$(call FUNC_MAKE_INIT) \
	&& docker compose \
	-f container/docker-compose.yml \
	exec \
	backend \
	bash

## ============================================================================
## Python Commands

gen-requirements: ## generate requirements.txt by poetry
	$(call FUNC_MAKE_INIT) \
	&& cd src \
	&& poetry export \
		--without-hashes \
		--format requirements.txt \
		--output requirements.txt \
	&& poetry export \
		--with dev \
		--without-hashes \
		--format requirements.txt \
		--output requirements_dev.txt \
	&& cd -

define FUNC_MAKE_INIT
	if [ -n "$$(command -v hr)" ]; then hr -; else echo "-----";fi \
	&& echo "⚙️ Running Makefile target: ${MAKECMDGOALS}"
endef
