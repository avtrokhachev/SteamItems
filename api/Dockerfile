FROM ubuntu:latest

RUN apt-get update
RUN apt upgrade -y
RUN apt install python3 python3-pip sudo wget -y

WORKDIR src/
COPY . .

RUN sudo mkdir /etc/configs
RUN sudo mv configs/prod_config.yaml /etc/configs/config.yaml

RUN make install
RUN pip install -r requirements.txt --break-system-packages

ENTRYPOINT ["sudo", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port",  "80", "--env-file", "configs/prod_envs.env"]
