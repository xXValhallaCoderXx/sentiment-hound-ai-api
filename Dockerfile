FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --find-links https://download.pytorch.org/whl/torch_stable.html

COPY . .
