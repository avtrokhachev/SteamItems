output "vpc_network" {
  value = yandex_vpc_network.network-database.id
}

output "vpc_subnet" {
  value = yandex_vpc_subnet.subnet-database.id
}