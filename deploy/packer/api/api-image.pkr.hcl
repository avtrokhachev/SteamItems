packer {
  required_plugins {
    yandex = {
      version = "~> 1"
      source  = "github.com/hashicorp/yandex"
    }
    docker = {
      version = ">= 1.0.8"
      source = "github.com/hashicorp/docker"
    }
  }
}

source "yandex" "steam-items-api" {
   folder_id           = "b1g68mcmoms86hiq32hh"
   source_image_family = "ubuntu-2004-lts"
   ssh_username        = "ubuntu"
   use_ipv4_nat        = "true"
   image_description   = "api for steam_items project"
   image_family        = "ubuntu-2004-lts"
   image_name          = "steam-items-api"
   subnet_id           = "e9bnftur59a85c304t34"
   disk_type           = "network-ssd"
   zone                = "ru-central1-a"
 }

 build {
   sources = ["source.yandex.steam-items-api"]

   provisioner "shell" {
     inline = ["export DEBIAN_FRONTEND=noninteractive",
           "sudo apt-get update -y",
           "sudo apt-get install -y docker.io",
           "sudo systemctl start docker",
           "sudo docker pull cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_api:latest",
           "sudo docker run --detach --publish 80:80 cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_api:latest"]
   }

 }