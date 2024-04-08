import os
from typing import Optional

import yaml

from .constants import (
    DEFAULT_CONFIG_NAME,
    DEFAULT_CONFIGS_DIR,
    DEFAULT_DEV_CONFIG_DIR,
    DEFAULT_DEV_CONFIG_NAME,
    State,
)


def get_configs_dir() -> str:
    if os.getenv(State.IN_CONTAINER.value):
        return DEFAULT_CONFIGS_DIR
    else:
        return DEFAULT_DEV_CONFIG_DIR


def get_config_name() -> str:
    if os.getenv(State.IN_CONTAINER.value):
        return DEFAULT_CONFIG_NAME
    else:
        return DEFAULT_DEV_CONFIG_NAME


def get_config(
    name: Optional[str] = None,
    dir: Optional[str] = None,
) -> dict:
    if name is None:
        name = get_config_name()
    if dir is None:
        dir = get_configs_dir()

    path = os.path.join(dir, name)
    with open(path, "r") as stream:
        return yaml.safe_load(stream=stream)


def set_config(
    config: dict,
    name: Optional[str] = None,
    dir: Optional[str] = None,
) -> None:
    if name is None:
        name = get_config_name()
    if dir is None:
        dir = get_configs_dir()

    path = os.path.join(dir, name)
    with open(path, "w") as cfg:
        yaml.safe_dump(config, cfg)


def get_value(
    key: str,
    name: Optional[str] = None,
    dir: Optional[str] = None,
):
    if name is None:
        name = get_config_name()
    if dir is None:
        dir = get_configs_dir()

    config = get_config(
        name=name,
        dir=dir,
    )

    key = key.split(".")
    for k in key:
        if not config or k not in config:
            return None
        config = config.get(k, None)

    return config


def set_value(
    key: str,
    value,
    name: Optional[str] = None,
    dir: Optional[str] = None,
) -> None:
    if name is None:
        name = get_config_name()
    if dir is None:
        dir = get_configs_dir()

    if value is None:
        return

    config = get_config(
        name=name,
        dir=dir,
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
        name=name,
        dir=dir,
    )
