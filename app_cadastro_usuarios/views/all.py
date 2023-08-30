from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from app_cadastro_usuarios.forms import (AuthorRecipeForm, LoginForm,
                                         RegisterForm)
from recipes.models import Recipe


def register_view(request):
    Registro_digitado_pelo_usuario_POST = request.session.get("Registro_digitado_pelo_usuario_POST", None)
    form = RegisterForm(Registro_digitado_pelo_usuario_POST)

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
    request.session["Registro_digitado_pelo_usuario_POST"] = POST
    form = RegisterForm(POST)
    print(POST)

    #valida o formulario recebido pelo POST que foi guardado na session do navegador do usuario
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Cadastro Realizado com sucesso")

        del(request.session["Registro_digitado_pelo_usuario_POST"])
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
    return redirect("cadastro:dashboard")


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
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user,

    )
    return render(request, "app_cadastro_usuarios/pages/dashboard.html",  context={
        "recipes": recipes,
        "search": False,

    })


@login_required(login_url="cadastro:login", redirect_field_name="next")
def dashboard_recipe_create_new(request):
    
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        #Agora, o form é válido e eu posso tentar salvar
        recipe = form.save(commit=False)

        recipe.author = request.user

        recipe.preparation_steps_is_html = False
        recipe.is_published = False
        recipe.save()

        messages.success(request, "Sua receita foi salva com sucesso!")
        return redirect(reverse("cadastro:dashboard_recipe_create_new"))


    return render(request, "app_cadastro_usuarios/pages/dashboard_recipe.html",  context={
        "search": False,
        "type_screen": "Register",
        "form": form

    })


@login_required(login_url="cadastro:login", redirect_field_name="next")
def dashboard_recipe_delete(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    # print(POST)
    id = POST.get("id")

    recipe = Recipe.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,

    ).first()

    if not recipe:
        raise Http404()
    
    recipe.delete()
    messages.success(request, "Deletado com sucesso")
    return redirect(reverse("cadastro:dashboard"))










# @login_required(login_url="cadastro:login", redirect_field_name="next")
# def dashboard_recipe_edit(request, id):
#     recipe = Recipe.objects.filter(
#         is_published=False,
#         author=request.user,
#         pk=id,

#     ).first()

#     if not recipe:
#         raise Http404()
    
#     form = AuthorRecipeForm(
#         data=request.POST or None,
#         files=request.FILES or None,
#         instance=recipe
#     )

#     if form.is_valid():
#         #Agora, o form é válido e eu posso tentar salvar
#         recipe = form.save(commit=False)

#         recipe.author = request.user

#         recipe.preparation_steps_is_html = False
#         recipe.is_published = False
#         recipe.save()

#         messages.success(request, "Sua receita foi salva com sucesso!")
#         return redirect(reverse("cadastro:dashboard_recipe_edit", args=(id, )))


#     return render(request, "app_cadastro_usuarios/pages/dashboard_recipe.html",  context={
#         "search": False,
#         "type_screen": "Register",
#         "form": form

#     })