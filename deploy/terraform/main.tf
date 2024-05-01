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
  depends_on = [module.api-network, module.api-static-addr]
}

module "worker" {
  source = "./modules/worker"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
  image_id = var.api_image_id
  api_subnet_id = module.api-network.vpc_subnet
  depends_on = [module.api-network, module.api-static-addr]
}

module "database" {
  source = "./modules/database"
  folder_id = var.folder_id
  cloud_id = var.cloud_id
  network_id = module.api-network.vpc_network
  subnet_id = module.api-network.vpc_subnet
  depends_on = [module.api-network]
}