FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN ["pip", "install", "discord.py"]

RUN ["pip", "install", "dotenv"]

CMD ["python", "main.py"]
