resource "yandex_logging_group" "steam-logging" {
  name      = "steam-items-logs"
  folder_id = var.folder_id
  retention_period = "72h"
}