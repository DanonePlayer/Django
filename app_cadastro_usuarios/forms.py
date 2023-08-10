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
            "password must have at least one uppercase letter,"
            "one lowercase letter and one number. The length shoud be at least 8 characters."
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
            "username": "Obrigatório. 8 caracteres ou mais. Letras, números e @/./+/-/_ apenas.",
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
    
    def clean_password(self):#validaespecifico do campo
        data = self.cleaned_data.get("password")

        if"atencion" in data:
            raise ValidationError(
                "DIGITO ERRADO",
                code="invalid",
                
            )

        print(data)

        return data
    
    def clean(self):#valida todo o formulario
        cleaned_data = super().clean()
