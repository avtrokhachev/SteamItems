import os

from src.functions import get_settings


def test_settings():
    assert os.environ.get("RUNNING_TESTS", False)
    assert "PostgresOptions" in get_settings().keys()
