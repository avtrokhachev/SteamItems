resource "yandex_vpc_network" "network-database" {
  name = "network-database"
}

resource "yandex_vpc_subnet" "subnet-database" {
  name           = "subnet-database"
  zone           = "ru-central1-a"
  network_id     = "${yandex_vpc_network.network-database.id}"
  v4_cidr_blocks = ["10.5.0.0/16"]
}