stopAll:
	# docker stop $$(docker ps -aq)
	@if [ "`docker ps -q`" != "" ]; then docker stop $(docker ps -q); else echo "No running containers to stop"; fi

removeAll:
	# docker rm $$(docker ps -aq)
    @if [ "`docker ps -aq`" != "" ]; then docker rm $(docker ps -aq); else echo "No stopped containers to remove"; fi

clean: stopAll removeAll

build:
	docker build -t insecure_bank_app .

run:
	docker run -p 8080:8080 -it insecure_bank_app

restart: clean build run