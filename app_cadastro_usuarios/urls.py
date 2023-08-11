from django.urls import path

from recipes import views as viewrecipe

from . import views

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

app_name = "cadastro"

urlpatterns = [
    path("", views.register, name="register"),
    path("create/", views.register_create, name="create"),
    path("recipes/", viewrecipe.home, name="recipe"),
]
