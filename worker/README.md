# WARNING #

This service was written about a year ago and have not benn modified since then.
Code is old and deprecated, tests coverage also sucks.
Just trust than it's working until further refactoring


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
docker run --detach --publish 80:80 steam_items_main:latest
```