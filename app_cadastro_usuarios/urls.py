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
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/recipe/new", views.DashboardRecipeCreated.as_view(), name="dashboard_recipe_create_new"),
    path("dashboard/recipe/delete", views.DashboardRecipeDelete.as_view(), name="dashboard_recipe_delete"),
    path("dashboard/recipe/<int:id>/edit", views.DashboardRecipeEdit.as_view(), name="dashboard_recipe_edit"),
    
]
