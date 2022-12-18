FROM python:3.10.9-slim-buster

ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3","-u","consumer.py"]