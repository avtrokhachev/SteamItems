output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-2.network_interface.0.ip_address
}
