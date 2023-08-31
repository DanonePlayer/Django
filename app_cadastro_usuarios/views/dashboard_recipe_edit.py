from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from app_cadastro_usuarios.forms import AuthorRecipeForm
from recipes.models import Recipe


@method_decorator(
    login_required(login_url="cadastro:login", redirect_field_name="next"),
    name="dispatch"
)
class DashboardRecipeEdit(View):

    def get_recipe(self, id):
        recipe = None
        if id is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,

            ).first()

            if not recipe:
                raise Http404()

            return recipe

    def render_recipe(self, form):

        return render(self.request, "app_cadastro_usuarios/pages/dashboard_recipe.html",  context={
            "search": False,
            "type_screen": "Register",
            "form": form

        })

    def get(self, request, id):
        recipe = self.get_recipe(id)
        
        form = AuthorRecipeForm(
            instance=recipe
        )

        return self.render_recipe(form)
    


    
    def post(self, request, id):
        recipe = self.get_recipe(id)
        
        form = AuthorRecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )

        if form.is_valid():
            #Agora, o form é válido e eu posso tentar salvar
            recipe = form.save(commit=False)

            recipe.author = request.user

            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            recipe.save()

            messages.success(request, "Sua receita foi salva com sucesso!")
            return redirect(reverse("cadastro:dashboard_recipe_edit", args=(id, )))


        return self.render_recipe(form)