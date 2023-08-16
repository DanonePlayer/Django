from django.urls import path

from recipes import views as viewrecipe

from . import views

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

app_name = "cadastro"

urlpatterns = [
    path("", views.register_view, name="register"),
    path("create/", views.register_create, name="register_create"),
    path("recipes/", viewrecipe.home, name="recipe"),
    path("login/", views.login_view, name="login"),
    path("login/create/", views.login_create, name="login_create"),
]
