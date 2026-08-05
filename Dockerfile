# Don't Remove Credit @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

FROM python:3.10.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Change EXPOSE and CMD to port 8080
EXPOSE 8080

CMD gunicorn --bind 0.0.0.0:8080 app:app & python3 bot.py
