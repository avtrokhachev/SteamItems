import pytest

import database


@pytest.fixture(scope="function", autouse=True)
def start_database():
    database.start_and_clear_for_test()

    yield
