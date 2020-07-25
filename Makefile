app_name = neapp

build:
	@docker build -t $(app_name) .

run:
	docker run --detach -p8000:8000 $(app_name)

kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker kill
