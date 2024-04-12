output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "vpc_network" {
  value = yandex_vpc_network.network-api.id
}

output "vpc_subnet" {
  value = yandex_vpc_subnet.subnet-api.id
}
