resource "yandex_vpc_network" "network-api" {
  name = "network-api"
}

resource "yandex_vpc_subnet" "subnet-api" {
  name           = "subnet-api"
  zone           = "ru-central1-a"
  network_id     = "${yandex_vpc_network.network-api.id}"
  v4_cidr_blocks = ["10.2.0.0/16"]
}