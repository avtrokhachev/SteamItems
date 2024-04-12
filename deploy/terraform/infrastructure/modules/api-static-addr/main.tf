#resource "yandex_vpc_address" "addr" {
#  name                = "api-steam-items-static-ip-addr"
#  deletion_protection = "false"
#  external_ipv4_address {
#    zone_id = "ru-central1-a"
#  }
#}

terraform import yandex_vpc_address.addr address_id