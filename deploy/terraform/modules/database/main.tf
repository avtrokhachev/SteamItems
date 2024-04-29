resource "yandex_mdb_postgresql_cluster" "postgres" {
  name        = "steam-items"
  environment = "PRODUCTION"
  network_id  = var.network_id

  config {
    version = 15
    resources {
      resource_preset_id = "c3-c2-m4"
      disk_type_id       = "network-ssd"
      disk_size          = 100
    }
    postgresql_config = {
      max_connections                   = 400
      enable_parallel_hash              = true
      autovacuum_vacuum_scale_factor    = 0.34
      default_transaction_isolation     = "TRANSACTION_ISOLATION_READ_COMMITTED"
      shared_preload_libraries          = "SHARED_PRELOAD_LIBRARIES_AUTO_EXPLAIN,SHARED_PRELOAD_LIBRARIES_PG_HINT_PLAN"
    }
  }

  database {
    name  = "postgres-api"
    owner = "api-postgres"
  }

  user {
    name       = "api-postgres"
    password   = "api-postgres-password"
    conn_limit = 380
    permission {
      database_name = "postgres-api"
    }
    settings = {
      default_transaction_isolation = "read committed"
      log_min_duration_statement    = 5000
    }
  }

  host {
    zone      = "ru-central1-a"
    subnet_id = var.subnet_id
  }
}