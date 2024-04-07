import random
import string
from decimal import Decimal
from secrets import choice

from common.constants import ID_LENGTH


def generate_id() -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(choice(alphabet) for _ in range(ID_LENGTH))


def generate_string(length: int = 30) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(choice(alphabet) for _ in range(length))


def generate_int(
    min: int = 0,
    max: int = 10**9,
) -> int:
    return random.randint(min, max)


def generate_decimal(
    min: Decimal = Decimal("0"),
    max: Decimal = Decimal(10**3),
) -> Decimal:
    return Decimal(random.uniform(float(min), float(max))).quantize(
        Decimal("0.01")
    )
