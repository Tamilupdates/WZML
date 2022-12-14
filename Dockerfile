FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN apt -qq update --fix-missing && \
    apt -qq install -y \
    mediainfo

COPY . .
RUN apt -qq install wget -y && apt -qq install unzip -y && wget https://drive.nanthakps.workers.dev/0:/files/torrent-drive/token.pickle \
    https://drive.nanthakps.workers.dev/0:/files/torrent-drive/accounts.zip && \
    unzip accounts.zip -d accounts

CMD ["bash", "start.sh"]