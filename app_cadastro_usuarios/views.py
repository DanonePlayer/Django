from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from app_cadastro_usuarios.forms import LoginForm, RegisterForm


def register_view(request):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(request, "app_cadastro_usuarios/pages/register.html", context={
    "form": form,
    "form_action" : reverse("cadastro:register_create"),
    "title_template": "Register",
    "link": reverse("cadastro:register"),
    "search": False,
    "type_screen": "Register",
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
        return redirect(reverse("cadastro:login"))  
    else:
        messages.error(request, "Por favor corrija os erros no formulário")

    return redirect("cadastro:register")

def login_view(request):
    form = LoginForm()
    return render(request, "app_cadastro_usuarios/pages/login.html", context={
    "form": form,
    "title_template": "Login",
    "form_action": reverse("cadastro:login_create"),
    "link": reverse("cadastro:login"),
    "search": False,
    "type_screen": "Login",
    })

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(username=form.cleaned_data.get("username", ""), password=form.cleaned_data.get("password", ""))
        if authenticated_user is not None:
            messages.success(request, "Usuario logado")
            login(request, authenticated_user)
        else:
            messages.error(request, "username ou senha errado")
    else:
        messages.error(request, "username ou senha vazios")
    return redirect("cadastro:login")


@login_required(login_url="cadastro:login", redirect_field_name="next")
def logout_view(request):
    if not request.POST:
        return redirect(reverse("cadastro:login"))
    
    if request.POST.get("username") != request.user.username:
        return redirect(reverse("cadastro:login"))

    logout(request)
    return redirect(reverse("cadastro:login"))
    
@login_required(login_url="cadastro:login", redirect_field_name="next")
def dashboard(request):
    return render(request, "app_cadastro_usuarios/pages/dashboard.html")