from django import forms
from rePet.models import Cadastro, Usuario

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'sobrenome',
            'email',
            'senha',
            'telefone',
            'endereco'
        ]

class LoginUsuario(forms.ModelForm):
    email = Usuario
    senha = Usuario
    class Meta:
        model = Usuario
        fields = [
            'email',
            'senha'
        ]