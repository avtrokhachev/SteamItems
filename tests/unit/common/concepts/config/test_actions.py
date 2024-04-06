import pytest

from common.concepts import config


class TestGetValue:
    ############
    # FIXTURES #
    ############

    @pytest.fixture(scope="function")
    def prepare_config(self):
        old_value = config.get_value("test_config")

        config.set_value("test_config", "third")
        yield
        config.set_value("test_config", old_value)

    #########
    # TESTS #
    #########

    def test_ok(self, prepare_config):
        value = config.get_value("test_config")

        assert value == "third"


class TestSetValue:
    ############
    # FIXTURES #
    ############

    @pytest.fixture(scope="function")
    def prepare_config(self):
        old_value = config.get_value("test_config")

        config.set_value("test_config", "third")
        yield
        config.set_value("test_config", old_value)

    #########
    # TESTS #
    #########

    def test_ok(self, prepare_config):
        config.set_value("test_config", "second")

        new_value = config.get_value("test_config")
        assert new_value == "second"
