FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 8083

CMD ["python", "server.py"]