import os

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


class TestGetConfigsDir:
    ############
    # FIXTURES #
    ############

    @pytest.fixture(scope="function")
    def set_production_env(self):
        os.environ[config.constants.State.PRODUCTION.value] = "true"
        yield
        os.environ.pop(config.constants.State.PRODUCTION.value)

    @pytest.fixture(scope="function")
    def set_testing_env(self):
        os.environ[config.constants.State.TESTING.value] = "true"
        yield
        os.environ.pop(config.constants.State.TESTING.value)

    #########
    # TESTS #
    #########

    def test_correctly_gets_dir_for_dev_env(self):
        result = config.get_configs_dir()

        assert result == config.constants.DEFAULT_DEV_CONFIG_DIR

    def test_correctly_gets_dir_for_production(
        self,
        set_production_env,
    ):
        result = config.get_configs_dir()

        assert result == config.constants.DEFAULT_CONFIGS_DIR

    def test_correctly_gets_dir_for_testing(
        self,
        set_testing_env,
    ):
        result = config.get_configs_dir()

        assert result == config.constants.DEFAULT_CONFIGS_DIR


class TestGetConfigsName:
    ############
    # FIXTURES #
    ############

    @pytest.fixture(scope="function")
    def set_production_env(self):
        os.environ[config.constants.State.PRODUCTION.value] = "true"
        yield
        os.environ.pop(config.constants.State.PRODUCTION.value)

    @pytest.fixture(scope="function")
    def set_testing_env(self):
        os.environ[config.constants.State.TESTING.value] = "true"
        yield
        os.environ.pop(config.constants.State.TESTING.value)

    #########
    # TESTS #
    #########

    def test_correctly_gets_name_for_dev_env(self):
        result = config.get_config_name()

        assert result == config.constants.DEFAULT_DEV_CONFIG_NAME

    def test_correctly_gets_dir_for_production(
        self,
        set_production_env,
    ):
        result = config.get_config_name()

        assert result == config.constants.DEFAULT_CONFIG_NAME

    def test_correctly_gets_dir_for_testing(
        self,
        set_testing_env,
    ):
        result = config.get_config_name()

        assert result == config.constants.DEFAULT_CONFIG_NAME
