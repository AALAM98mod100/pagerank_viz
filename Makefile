build:
	docker-compose build
run:
	docker-compose up -d
test:
	docker-compose exec server ./manage.py test