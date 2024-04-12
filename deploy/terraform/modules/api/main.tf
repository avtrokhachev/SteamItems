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
    subnet_id      = var.api_subnet_id
    nat            = true
    nat_ip_address = var.api_nat_ip_address
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/yc-personal.pub")}"
    user-data = file("${path.module}/cloud_config.yaml")
  }
}