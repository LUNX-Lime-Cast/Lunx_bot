FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN ["pip", "install", "discord.py"]

CMD ["python", "main.py"]
