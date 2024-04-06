import os
from pathlib import Path

import yaml

from .constants import DEFAULT_CONFIG_PATH

CONFIG_DIR_PATH = str(
    Path(os.path.dirname((os.path.realpath(__file__)))).parents[2]
)


def get_config(
    path: str = DEFAULT_CONFIG_PATH,
) -> dict:
    path = os.path.join(CONFIG_DIR_PATH, path)
    with open(path, "r") as stream:
        return yaml.safe_load(stream=stream)


def set_config(
    config: dict,
    path: str = DEFAULT_CONFIG_PATH,
) -> None:
    path = os.path.join(CONFIG_DIR_PATH, path)
    with open(path, "w") as cfg:
        yaml.safe_dump(config, cfg)


def get_value(
    key: str,
    path: str = DEFAULT_CONFIG_PATH,
):
    config = get_config(path)

    key = key.split(".")
    for k in key:
        if not config or k not in config:
            return None
        config = config.get(k, None)

    return config


def set_value(
    key: str,
    value,
    path: str = DEFAULT_CONFIG_PATH,
) -> None:
    if value is None:
        return

    config = get_config(
        path=path,
    )
    key = key.split(".")

    cursor = config
    for k in key[:-1]:
        if k not in cursor:
            cursor[k] = dict()
        cursor = cursor[k]

    cursor[key[-1]] = value

    set_config(
        config=config,
        path=path,
    )
