from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "app_cadastro_usuario/home.html", context={"name": "carlos",})