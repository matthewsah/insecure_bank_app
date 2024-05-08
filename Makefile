stopAll:
	docker stop $$(docker ps -aq)

removeAll:
	docker rm $$(docker ps -aq)

clean: stopAll removeAll

build:
	docker build -t insecure_bank_app .

run:
	docker run -p 8080:8080 -it insecure_bank_app

restart: clean build run