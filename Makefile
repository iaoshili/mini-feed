.PHONY: test
test:
	docker-compose exec users python -m pytest "project/tests" -p no:warnings

.PHONY: run
run:
	docker-compose up --build -d

.PHONY: builddb
builddb:
	docker-compose exec users python manage.py recreate_db
	docker-compose exec users python manage.py seed_db


.PHONY: shell
shell:
	docker exec -it mini-feed_users_1 sh
