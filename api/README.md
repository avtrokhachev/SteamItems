# General information #
This microservice is responsible for saving/working with SteamItems. It is the main service of the project, users requests are also handled here.

# How to setup project #

1. Setup and activate venv
```
python3 -m venv venv
source venv/bin/activate
```
2. Install requirements
```
pip3 install -r requirements.txt
```
3. Install packages
```
make install_dev
```
4. Edit config path and database url in `common/common/concepts/config/constants.py`
5. Make sure, that everything is working correct by running tests
```
make run_tests
```

# How to build and run docker image #

1. Edit production config `configs/prod_config.yaml`
2. Build docker image
```
docker build -t steam_items_main .
```
3. Start docker container
```
docker run --detach --publish 80:80 steam_items_main:latest
```