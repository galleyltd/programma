FROM python:3.6-alpine3.6

WORKDIR /usr/src/programma/server

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

COPY . .
CMD python server.py
