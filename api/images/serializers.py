"""Serializers for the images app."""

from images.models import Resizing
from rest_framework import serializers

from .producer import send_to_resize_service


# pylint: disable=protected-access
class ResizingSerializer(serializers.ModelSerializer):
    """Serializer for the resizing model."""

    def create(self, validated_data):
        """Override create to properly set instance id for file upload keys and trigger resize."""
        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create()
        instance = self.update(instance, validated_data)

        send_to_resize_service(instance)

        return instance

    class Meta:
        model = Resizing
        fields = ['id', 'input', 'output']
        read_only_fields = ['id']
