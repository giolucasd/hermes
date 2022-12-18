"""Producer for RabbitMQ resizing queue."""

import json
from base64 import b64encode

import pika

from .models import Resizing

# TODO: refactor architecture to improve queue informations storing.
RABBIT_USER = "user"
RABBIT_PWD = "password"
RABBIT_HOST = "queue"
RABBIT_PORT = 5672
RABBIT_VHOST = "/"
EXCHANGE_NAME = "resizing"
QUEUE_NAME = "resizing_queue"


def send_to_resize_service(instance: Resizing) -> None:
    """Send message to queue in order to trigger resizing processing."""
    print(f"Sending message for Resizing #id={instance.id} to queue!")

    queue_credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PWD)
    queue_params = pika.ConnectionParameters(
        RABBIT_HOST,
        RABBIT_PORT,
        RABBIT_VHOST,
        queue_credentials,
    )

    connection = pika.BlockingConnection(queue_params)
    channel = connection.channel()

    # TODO: refactor the service to share file storage with API.
    # That would avoid the need to send images through the network.
    body = json.dumps(
        {
            "id": instance.id,
            "input": b64encode(instance.input.read()).decode("utf-8"),
        }
    )
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=QUEUE_NAME,
        body=body,
    )

    connection.close()
