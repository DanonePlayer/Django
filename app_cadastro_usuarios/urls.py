from django.urls import path
from app_cadastro_usuarios.views import home

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST



urlpatterns = [
    path("", home),
]
