import enum

DEFAULT_CONFIGS_DIR = "/etc/configs"
DEFAULT_CONFIG_NAME = "config.yaml"
DEFAULT_DEV_CONFIG_DIR = "/Users/avtrokhachev/Documents/projects/SteamItems/configs"  # TODO: awful, fix
DEFAULT_DEV_CONFIG_NAME = "config.yaml"


class State(enum.Enum):
    IN_CONTAINER = "IN_CONTAINER"
    TESTING = "TESTING"
