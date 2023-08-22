from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe


class AuthorRecipeForm(forms.ModelForm):




    #Adiciona ao campo uma class do CSS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["preparation_steps"].widget.attrs.update({'class': 'span-2'})


    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "preparation_time",
            "preparation_time_unit",
            "servings",
            "servings_unit",
            "preparation_steps",
            "cover",
        ]
        widgets = {
            "cover": forms.FileInput(attrs={
                "class": "span-2"

            }),
            "servings_unit": forms.Select(
                choices=(
                    ("Porções", "Porções"),
                    ("Pedaços", "Pedaços"),
                    ("Pessoas", "Pessoas"),
                )
            ),
            "preparation_time_unit": forms.Select(
                choices=(
                    ("Minutos", "Minutos"),
                    ("Horas", "Horas"),
                )
            )
        }

    def clean(self):#valida todo o formulario
        self._errors_recipe_form = defaultdict(list)
        cleaned_data = super().clean()

        title = cleaned_data.get("title")

        if len(title) < 5:
            self._errors_recipe_form["title"].append("Seu titulo tem menos de 5 caracteres")


        if self._errors_recipe_form:
            raise ValidationError(self._errors_recipe_form)