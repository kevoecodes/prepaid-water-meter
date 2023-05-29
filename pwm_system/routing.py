from channels.routing import ProtocolTypeRouter, URLRouter
#from django.conf.urls import url
from django.urls import re_path
#from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from Users_Management.consumer import User_DevUpdates_Consumer

application = ProtocolTypeRouter({
    #Empty 
    #"http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
                URLRouter(
                [
                    re_path(r"^user-socket-portal/(?P<deviceNo>)", User_DevUpdates_Consumer.as_asgi()),
                    #url(r"^user-notifications-portal/(?P<deviceNo>)", User_Dev_Portal.as_asgi()),
                    #url(r"^user-notifications-portal/(?P<deviceNo>)", User_Dev_Portal.as_asgi()),
                ]
            )
        )
    )
})