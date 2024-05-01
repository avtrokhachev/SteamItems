resource "yandex_compute_instance_group" "worker-ig" {
  name = "worker-ig"
  folder_id = var.folder_id
  service_account_id = "ajekqdk2bmvjq29993jl"

  instance_template {
    platform_id = "standard-v1"

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
      subnet_ids      = [var.api_subnet_id]
      nat = true
    }

    metadata = {
      ssh-keys = "ubuntu:${file("~/.ssh/yc-personal.pub")}"
      user-data = file("${path.module}/cloud_config.yaml")
    }
  }

  scale_policy {
    fixed_scale {
      size = 3
    }
  }

  allocation_policy {
    zones = ["ru-central1-a"]
  }

  deploy_policy {
    max_unavailable = 3
    max_creating = 3
    max_expansion = 3
    max_deleting = 3
  }
}
