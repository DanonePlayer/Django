from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from app_cadastro_usuarios.forms import AuthorRecipeForm


@method_decorator(
    login_required(login_url="cadastro:login", redirect_field_name="next"),
    name="dispatch"
)
class DashboardRecipeCreated(View):
    def get(self, request):
        form = AuthorRecipeForm()
        return self.render_recipe(form)

    def post(self, request):
        form = AuthorRecipeForm(
            data=self.request.POST or None,
            files=self.request.FILES or None,
        )

        if form.is_valid():
            #Agora, o form é válido e eu posso tentar salvar
            recipe = form.save(commit=False)

            recipe.author = self.request.user

            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            recipe.save()

            messages.success(self.request, "Sua receita foi salva com sucesso!")
            return redirect(reverse("cadastro:dashboard_recipe_edit", args=(recipe.id, )))
            
        
        return self.render_recipe(form)
    
    
    def render_recipe(self, form):        
        return render(self.request, "app_cadastro_usuarios/pages/dashboard_recipe.html",  context={
        "search": False,
        "type_screen": "Register",
        "form": form
        })


