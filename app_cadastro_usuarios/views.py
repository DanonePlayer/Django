from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "app_cadastro_usuario/pages/login.html", context={"name": "carlos",})