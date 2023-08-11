from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from app_cadastro_usuarios.forms import RegisterForm


def login(request):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(request, "app_cadastro_usuarios/pages/register.html", context={
    "name": "carlos",
    "form": form
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        data = form.save(commit=False)
        print(data)
        form.save()
        messages.success(request, "PARABENS OLOROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        del(request.session["register_form_data"])

    return redirect("cadastro:login")