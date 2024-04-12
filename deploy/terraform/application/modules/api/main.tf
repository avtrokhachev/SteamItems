resource "yandex_compute_instance" "vm-1" {
  name = "steam-items-api"
  platform_id = "standard-v1"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id      = yandex_vpc_subnet.subnet-api.id
    nat            = true
    nat_ip_address = yandex_vpc_address.addr.external_ipv4_address[0].address
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/yc-personal.pub")}"
    user-data = file("${path.module}/cloud_config.yaml")
  }
}