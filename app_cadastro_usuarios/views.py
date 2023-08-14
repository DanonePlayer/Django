from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from app_cadastro_usuarios.forms import RegisterForm


def register(request):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(request, "app_cadastro_usuarios/pages/register.html", context={
    "name": "carlos",
    "form": form,
    "form_action" : reverse("cadastro:create"),
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Cadastro Realizado com sucesso")
        del(request.session["register_form_data"])
    else:
        messages.error(request, "Por favor corrija os erros no formulário")

    return redirect("cadastro:register")