Build docker image
``docker build -t steam_items_main .``

Run docker container
``docker run --detach --publish 80:80 steam_items_main:latest``