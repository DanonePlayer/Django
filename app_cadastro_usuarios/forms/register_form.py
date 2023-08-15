import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Digite sua senha"
        }),
        error_messages={
            "required": "A senha não deve estar vazia"
        },
        help_text=(
            "A senha deve ter pelo menos uma letra maiúscula, uma letra minúscula e um número."
            "O comprimento deve ser de pelo menos 8 caracteres."
        )
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Repita sua senha"
        })
    )
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",            
        ]
        # exclude = ["first_name"]
        labels = { #nome dos campos acima do input
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "email": "Email",
            "password": "Password",
        }
        help_texts = {#frases de ajuda a baixo do label
            "email": "O e-mail digitado deve ser válido.",
            "username": "Obrigatório. 8 caracteres ou mais, contendo letras, números e @/./+/-/_ apenas.",
        }
        error_messages = {#frases de erros
            "username":{
                "required": "Este campo não pode estar vazio",
                "max_length": "Este campo contém menos de 8 caracteres",
                "invalid": "Este campo é inválido",
            }
        }
        widgets = {#frases dentro do campo do input para ajudar
            "username": forms.TextInput(attrs={
                "placeholder": "Digite seu nome de usuário aqui",
                "class": "text-input outra-classe",
            }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "Digite sua senha aqui",
            }),
        }
    
    def clean_username(self):#validaespecifico do campo
        regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
        username = self.cleaned_data.get("username")

        if not regex.match(username):
            raise ValidationError("Seu user contem menos de 8 caracteres", code="invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        users = User.objects.filter(email=email).exists()
        if users:
            raise ValidationError("Este email ja existe", code="invalid")
        return email

    def clean(self):#valida todo o formulario
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
        password2 = cleaned_data.get("password2")
        first_name = cleaned_data.get("first_name")


        if first_name in password:
            raise ValidationError({
                "password": "Sua senha não pode ser igual ao seu nome",
            })

        if password != password2:
            raise ValidationError({
                "password": "Erro, suas senhas não coicidem",
                "password2": "Erro, suas senhas não coicidem"

            })
        
        if not regex.match(password):
            raise ValidationError({
                "password": "Sua senha contem menos de 8 caracteres"
            })
