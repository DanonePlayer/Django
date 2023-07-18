from django.urls import path
from recipes import views

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST



urlpatterns = [
    path("", views.home),
    path("/receitas/<int:id>/", views.recipe),
]