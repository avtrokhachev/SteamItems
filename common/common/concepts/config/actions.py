import os

import yaml

from .constants import DEFAULT_CONFIG_NAME, DEFAULT_CONFIGS_DIR


def get_config(
    name: str = DEFAULT_CONFIG_NAME,
    dir: str = DEFAULT_CONFIGS_DIR,
) -> dict:
    path = os.path.join(dir, name)
    with open(path, "r") as stream:
        return yaml.safe_load(stream=stream)


def set_config(
    config: dict,
    name: str = DEFAULT_CONFIG_NAME,
    dir: str = DEFAULT_CONFIGS_DIR,
) -> None:
    path = os.path.join(dir, name)
    with open(path, "w") as cfg:
        yaml.safe_dump(config, cfg)


def get_value(
    key: str,
    name: str = DEFAULT_CONFIG_NAME,
    dir: str = DEFAULT_CONFIGS_DIR,
):
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
    name: str = DEFAULT_CONFIG_NAME,
    dir: str = DEFAULT_CONFIGS_DIR,
) -> None:
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
