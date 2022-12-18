"""Consumer for RabbitMQ resizing queue."""

import json
import time
from base64 import b64decode
from io import BytesIO
from typing import Any

import pika
import requests
from PIL import Image

# TODO: refactor architecture to improve queue informations storing.
RABBIT_USER = "user"
RABBIT_PWD = "password"
RABBIT_HOST = "queue"
RABBIT_PORT = 5672
RABBIT_VHOST = "/"
QUEUE_NAME = "resizing_queue"


# pylint: disable=unused-argument,invalid-name
def callback(ch: Any, method: Any, properties: Any, body: Any) -> None:
    """Callback that reads input, resize image and send it to API."""
    # TODO: refactor the service to share file storage with API.
    # That would avoid the need to send images through the network.

    input_data = json.loads(body)
    resizing_id = input_data["id"]
    resizing_input = input_data["input"]
    print(f"Received message for Resizing #id={resizing_id}!", flush=True)

    input_bytes = BytesIO(b64decode(resizing_input))
    input_ = Image.open(input_bytes)
    output_size = (384, 384)

    output = input_.resize(output_size)
    output_bytes = BytesIO()
    output.save(output_bytes, format="png")
    output_bytes.seek(0)
    url = f'http://api:8000/api/images/resizing/{resizing_id}/'
    output_data = {
        "output": (
            "output.png",
            output_bytes,
            "image/png"
        ),
    }

    response = requests.put(url, files=output_data, timeout=10)
    print(f'Sent output! Received status code #{response.status_code}.', flush=True)


queue_credentials = pika.PlainCredentials(username=RABBIT_USER, password=RABBIT_PWD)
queue_params = pika.ConnectionParameters(
    host=RABBIT_HOST,
    port=RABBIT_PORT,
    virtual_host=RABBIT_VHOST,
    credentials=queue_credentials,
)

# Try to connect to queue service for 2 minutes before giving up
# (queue service container might not be up yet)
CONNECT_MAX_RETRIES = 6
CONNECT_WAIT_TIME = 10

connection = None
for i in range(CONNECT_MAX_RETRIES):
    try:
        connection = pika.BlockingConnection(queue_params)
    except Exception as err:
        print(f"Error connecting to queue: {err.args[0]}", flush=True)
        time.sleep(CONNECT_WAIT_TIME)

if connection is None:
    print(f"Maximum retries exceeded while trying to connect to queue. Exiting!", flush=True)
    exit(1)

print("Connected succesfully to queue!", flush=True)
channel = connection.channel()
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
