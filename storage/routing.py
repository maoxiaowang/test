from django.urls import path

from storage.consumers import VolumeListConsumer


websocket_urlpatterns = [
    path('ws/storage/volume/', VolumeListConsumer),
]