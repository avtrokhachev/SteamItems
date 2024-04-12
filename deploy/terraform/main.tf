module "api-static-addr" {
  source = "./modules/api-static-addr"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
}

module "api-network" {
  source = "./modules/api-network"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
}

module "api" {
  source = "./modules/api"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
  image_id = var.api_image_id
  api_subnet_id = module.api-network.vpc_subnet
  api_nat_ip_address = module.api-static-addr.external_ipv4_address
}

#module "database" {
#  source = "./infrastructure/modules/database"
#  folder_id = "b1g68mcmoms86hiq32hh"
#  cloud_id = "b1gspes674hmubhe9acg"
#  network_id = module.api-network.vpc_network
#  subnet_id = module.api-network.vpc_subnet
#}