from django.urls import path

from recipes import views as viewrecipe

from . import views

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

app_name = "cadastro"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", viewrecipe.home, name="recipe"),
]
