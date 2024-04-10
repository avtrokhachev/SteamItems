prepare_tokens:
	export YC_TOKEN=$(yc iam create-token --profile personal)
	docker login \
  		--username iam \
  		--password $(YC_TOKEN) \
  		cr.yandex


build_docker_images:
	chmod +x deploy/docker/build_images.sh
	./deploy/docker/build_images.sh


build_packer_images:
	packer build deploy/packer/api/api-image.pkr.hcl
