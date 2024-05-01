import configparser
import os
from decimal import Decimal


def convert_to_dollars(raw_value: str) -> Decimal:
    if "$" not in raw_value:
        raise Exception(
            f"Price {raw_value} not in dollars. Contract violation."
        )

    cur_val = [i for i in raw_value]
    ans = []
    for i in cur_val:
        if "0" <= i <= "9" or i in ",.":
            ans.append(i)
    ans = "".join(ans)
    ans = ans.replace(",", ".")
    if len(ans) == 0:
        ans = "0"

    return Decimal(ans)


def get_settings() -> configparser.SectionProxy:
    in_container = os.environ.get("IN_A_DOCKER_CONTAINER", False)
    testing = os.environ.get("RUNNING_TESTS", False)
    if in_container:
        sect = "Container"
    elif testing:
        sect = "Testing"
    else:
        sect = "Development"

    path = "../Settings.ini"
    if os.path.isfile("Settings.ini"):
        path = "Settings.ini"

    parser = configparser.ConfigParser()
    parser.read(path)
    return parser[sect]
