FROM ubuntu:latest

RUN apt-get update
RUN apt upgrade -y
RUN apt install python3 python3-pip sudo -y

ENV IN_CONTAINER=true

WORKDIR src/
COPY . .

RUN sudo mkdir /etc/configs
RUN sudo mv configs/prod_config.yaml /etc/configs/config.yaml

RUN python3 -m pip install common/
RUN python3 -m pip install database/
RUN python3 -m pip install controllers/
RUN python3 -m pip install api/
RUN pip install -r requirements.txt

ENTRYPOINT ["sudo", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port",  "80"]
