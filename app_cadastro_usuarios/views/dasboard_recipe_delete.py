from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from recipes.models import Recipe


@method_decorator(
    login_required(login_url="cadastro:login", redirect_field_name="next"),
    name="dispatch"
)
class DashboardRecipeDelete(View):
    def post(self, request):
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