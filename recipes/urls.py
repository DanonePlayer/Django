from django.urls import path
from recipes.views import home

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST



urlpatterns = [
    path("", home),
]