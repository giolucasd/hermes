"""Views for the images app."""

from images.models import Resizing
from images.serializers import ResizingSerializer
from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet


class ResizingViewSet(RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    """Resizing images API View."""
    queryset = Resizing.objects.all()
    serializer_class = ResizingSerializer
