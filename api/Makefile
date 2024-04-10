# TODO: split into unit/functional/integration
TESTS_DIR = "tests/"

API_PACKAGE_NAME = "api"
CONTROLLERS_PACKAGE_NAME = "controllers"
DATABASE_PACKAGE_NAME = "database"
COMMON_PACKAGE_NAME = "common"

API_DIR = "$(API_PACKAGE_NAME)/"
CONTROLLERS_DIR = "$(CONTROLLERS_PACKAGE_NAME)/"
DATABASE_DIR = "$(DATABASE_PACKAGE_NAME)/"
COMMON_DIR = "$(COMMON_PACKAGE_NAME)/"


install:
	python3 -m pip install $(COMMON_DIR)
	python3 -m pip install $(DATABASE_DIR)
	python3 -m pip install $(CONTROLLERS_DIR)
	python3 -m pip install $(API_DIR)


install_dev:
	python3 -m pip install -e $(COMMON_DIR) --config-settings editable_mode=strict
	python3 -m pip install -e $(DATABASE_DIR) --config-settings editable_mode=strict
	python3 -m pip install -e $(CONTROLLERS_DIR) --config-settings editable_mode=strict
	python3 -m pip install -e $(API_DIR) --config-settings editable_mode=strict


uninstall:
	pip uninstall -y $(COMMON_PACKAGE_NAME)
	pip uninstall -y $(DATABASE_PACKAGE_NAME)
	pip uninstall -y $(CONTROLLERS_PACKAGE_NAME)
	pip uninstall -y $(API_PACKAGE_NAME)


activate_linters:
	pre-commit install
	pre-commit install-hooks


run_tests:
	pytest $(TESTS_DIR)
