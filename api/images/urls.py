"""Urls for images app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

rest_router = DefaultRouter()
rest_router.register(r'resizing', views.ResizingViewSet, basename='resizing')

urlpatterns = [
    path('api/images/', include(rest_router.urls)),
]
