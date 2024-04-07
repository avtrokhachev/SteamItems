# TODO: split into unit/functional/integration
TESTS_DIR = "tests/"

API_DIR = "api/"
CONTROLLERS_DIR = "controllers/"
DATABASE_DIR = "database/"
COMMON_DIR = "common/"


install_dev:
	python3 -m pip install -e $(COMMON_DIR)
	python3 -m pip install -e $(DATABASE_DIR)
	python3 -m pip install -e $(CONTROLLERS_DIR)
	python3 -m pip install -e $(API_DIR)

run_tests:
	pytest $(TESTS_DIR)
