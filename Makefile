.PHONY: init

init:
	@make down
	@make up
	@make ps
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
ps:
	docker-compose ps
test:
	# docker-compose run --rm core python src/manage.py test src
	docker-compose run --rm core python -m unittest
format:
	docker-compose run --rm core black .
lint:
	docker-compose run --rm core black . --check
shell:
	docker-compose exec core flask shell