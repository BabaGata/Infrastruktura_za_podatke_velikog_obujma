FROM python:3.10

WORKDIR /eksperimentalni

COPY img .
COPY requirements.txt .
COPY client.py .
COPY consumer.py .
COPY producer.py .
COPY server.py .
COPY wrapper_script.sh .

RUN pip install -r requirements.txt

CMD ["./wrapper_script.sh"]