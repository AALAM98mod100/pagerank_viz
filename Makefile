build:
	docker-compose build
run:
	docker-compose up -d
test:
	docker-compose exec server ./manage.py test
migrate:
	docker-compose exec server ./manage.py migrate
makemigrations:
	docker-compose exec server ./manage.py makemigrations
shell:
	docker-compose exec server ./manage.py shell_plus
logs:
	docker-compose logs -f server
stop:
	docker-compose down
clean:
	docker-compose down -v
	docker-compose rm
	docker volume prune
	docker network prune
	docker image prune
bash:
	docker-compose exec server bash