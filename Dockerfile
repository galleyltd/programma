FROM python:3.6-stretch

WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y software-properties-common \
	&& wget -qO - 'https://packages.confluent.io/deb/4.0/archive.key' | apt-key add - \
	&& add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/4.0 stable main" \
	&& apt-get install -y librdkafka-dev librdkafka1

COPY script.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "script.py" ]
