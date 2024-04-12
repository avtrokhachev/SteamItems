module "api-network" {
  source = "./infrastructure/modules/api-network"
  folder_id = "b1g68mcmoms86hiq32hh"
  cloud_id = "b1gspes674hmubhe9acg"
}

module "database" {
  source = "./infrastructure/modules/database"
  folder_id = "b1g68mcmoms86hiq32hh"
  cloud_id = "b1gspes674hmubhe9acg"
  network_id = module.api-network.vpc_network
  subnet_id = module.api-network.vpc_subnet
}