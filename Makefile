prepare_tokens:
	export YC_TOKEN=$(yc iam create-token --profile personal)
	docker login \
  		--username iam \
  		--password $(YC_TOKEN) \
  		cr.yandex


build_docker_images:
	chmod +x deploy/docker/build_images.sh
	./deploy/docker/build_images.sh
