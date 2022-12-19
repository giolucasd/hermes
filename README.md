# Hermes

Simple API, message queue, micro-service exploration.

## Description

The project is very simple: a REST API that receives an image, send it through a queue to another service that resize the given image to size 384x384.

![Arch-v1](static/arch-v1.png?raw=true)

## Setup

In order to run the project, you need docker with compose plugin installed.

Then, you just need to open a terminal in this project root directory (the same as docker-compose.yml file) and run:

```sh
docker compose up
```

Docker will then build the images for all three services and run a container for them. Once they are all started, you just need to open the API documentation in your browser at [http://localhost:8000/swagger-ui](http://localhost:8000/swagger-ui/).

## Usage

To verify the complete flow you will need to create a new resize wait for the image to be processed and copy the resized image (from the API container) to your local machine.

To create the resize request you can post an input image to */api/images/resizing/* endpoint.

To check if the image has already been resized you can check the detail endpoint with a get at */api/images/resizing/your-resizing-id*.

To copy the resized image you can use the following command:

```sh
docker cp api-container-id:/files/resizing/your-resizing-id/output.png ./
```
