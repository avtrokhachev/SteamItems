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

module "database-network" {
  source = "./modules/database-network"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
}

module "api" {
  source = "./modules/api"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
  image_id = var.api_image_id
#  api_subnet_id = module.api-network.vpc_subnet
  api_subnet_id = module.database-network.vpc_subnet
  api_nat_ip_address = module.api-static-addr.external_ipv4_address
}

module "database" {
  source = "./modules/database"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
  network_id = module.database-network.vpc_network
  subnet_id = module.database-network.vpc_subnet
}