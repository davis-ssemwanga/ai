from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/video/", consumers.MyWebSocketConsumer.as_asgi()),
]