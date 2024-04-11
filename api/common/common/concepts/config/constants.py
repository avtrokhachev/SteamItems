import enum

DEFAULT_CONFIGS_DIR = "/etc/configs"
DEFAULT_CONFIG_NAME = "config.yaml"
DEFAULT_DEV_CONFIG_DIR = (
    "/Users/avtrokhachev/Documents/projects/SteamItems/api/configs"
)
DEFAULT_DEV_CONFIG_NAME = "personal_config.yaml"


class State(enum.Enum):
    DEVELOPING = "DEVELOPING"
    PRODUCTION = "PRODUCTION"
    TESTING = "TESTING"
