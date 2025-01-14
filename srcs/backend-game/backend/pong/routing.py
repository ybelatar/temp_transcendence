from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path("click/", consumers.CountConsumer.as_asgi()),
    path("pong/game/<uuid:id>", consumers.PongConsumer.as_asgi()),
    path("pong/chat/<uuid:id>", consumers.ChatConsumer.as_asgi()),
	re_path(r"(?P<arg>(.*))", consumers.DefaultConsumer.as_asgi()) # Regex match any string even empty
]
