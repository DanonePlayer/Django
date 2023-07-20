from django.urls import path

from recipes import views

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST

# recipes-recipe
# recipes:recipe
app_name = 'recipes'


urlpatterns = [
    path("", views.home, name="home"),
    path("/receitas/<int:id>/", views.recipe, name="recipe"),
]