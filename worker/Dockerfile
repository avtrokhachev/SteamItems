FROM selenium/standalone-chrome:112.0

RUN sudo apt-get update
RUN sudo apt upgrade -y
RUN sudo apt install python3 python3-pip -y

WORKDIR src/
COPY . .

RUN sudo pip3 install -r requirements.txt

ENTRYPOINT ["python3", "src/main.py"]
