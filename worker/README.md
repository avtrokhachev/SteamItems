# WARNING #

This service was written about a year ago and have not been modified since then.
Code is old and deprecated, tests coverage also sucks.
Just trust than it's working until further refactoring

# General information #

This microservice is responsible for parsing SteamCommunityMarket to collect information about SteamItems.
After getting information about any SteamItem, he goes to API microservice to update information about it there.

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
3. Run worker
```
python3 src/main.py
```

# How to build and run docker image #

1. Edit production config `configs/prod_config.yaml`
2. Build docker image
```
docker build -t steam_items_main .
```
3. Start docker container
```
docker run --detach steam_items_main:latest
```