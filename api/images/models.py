"""Models for the images app."""

import os

from django.db import models


def input_upload_key(instance, filename):
    """Finds the input upload unique key for the given instance."""
    _, file_extension = os.path.splitext(filename)
    return f"files/resizing/{instance.id}/input{file_extension}"


def output_upload_key(instance, filename):
    """Finds the output upload unique key for the given instance."""
    _, file_extension = os.path.splitext(filename)
    return f"files/resizing/{instance.id}/output{file_extension}"


class Resizing(models.Model):
    """Received image resizing model."""

    input = models.ImageField(
        upload_to=input_upload_key,
        null=True,
        blank=True,
        editable=True,
    )
    output = models.ImageField(
        upload_to=output_upload_key,
        null=True,
        blank=True,
        editable=True,
    )
