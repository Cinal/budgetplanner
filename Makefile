PROJECT = budgetplanner
COMPOSE = -f docker/docker-compose.yml
COMPOSE_ENV ?= 'docker/local.compose.env'

BUILDKIT_EXPORTS ?= DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1
CFG=$(COMPOSE) -p $(PROJECT) --env-file ${COMPOSE_ENV}


.PHONY: poetryupdate
poetryupdate:
	docker rm -f budgetplanner_budgetplanner-run_1 || echo "... budgetplanner_budgetplanner-run_1 does not exist"
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) run --name budgetplanner_budgetplanner-run_1 --entrypoint bash budgetplanner -c 'poetry update -C "$$POETRY_RUN_PATH"'

.PHONY: build
build: ## Build project.
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) build

.PHONY: up
up: ## Run project.
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) up -d

.PHONY: down
down: ## Stop project.
	$(BUILDKIT_EXPORTS) docker-compose ${CFG} down

.PHONY: restart
restart: ## Restart.
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) down || true
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) up -d

.PHONY: clean
clean: ## Cleanup.
	$(BUILDKIT_EXPORTS) docker-compose ${CFG} down --remove-orphans -v

.PHONY: django
django: ## Django shell
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py shell -i ipython

.PHONY: migrate
migrate: ## Run migrations on db
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py migrate


.PHONY: collectstatic
collectstatic: ## Create django statics fiels
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py collectstatic


.PHONY: flushdb
flushdb: ## Create django statics fiels
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py flush

.PHONY: cacheclear
cacheclear: ## Django cache clear
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py shell -c "from django.core.cache import cache;cache.clear();print('Cache purged.')"

.PHONY:
logs: ## DOCKER: Containers logs.
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) logs -f


.PHONY: shell
shell: ## Shell
	docker exec -it $(PROJECT)-budgetplanner-1 bash

.PHONY: dbshell
dbshell: ## Psql client
	$(BUILDKIT_EXPORTS) docker-compose $(CFG) exec $(PROJECT)-database psql $(PROJECT) budgetplanner-user

.PHONY: demodata
demodata: ## Create demo data
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py demodata

.PHONY: makemigrations
makemigrations: ## Create migrations
	docker exec -it $(PROJECT)-budgetplanner-1 python manage.py makemigrations

.PHONY: superuser
superuser: ## Create demo data
	docker exec -it $(PROJECT)-budgetplanner-1 bash -c 'DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=adminpassword python manage.py createsuperuser --noinput'


.PHONY: init
init: build restart makemigrations migrate collectstatic demodata superuser ## Setup initial project data

 .PHONY: tests
tests: ## TESTS: Run tests.
	docker exec -it budgetplanner-budgetplanner-tests-1 bash -c "cd ../ && ./bin/tests.sh"

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nCommands:\n  make \033[1;32m\n"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
