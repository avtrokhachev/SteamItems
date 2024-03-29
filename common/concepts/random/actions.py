import string
from secrets import choice


def generate_id() -> str:
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(choice(alphabet) for _ in range(16))
