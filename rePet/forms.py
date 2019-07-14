from django import forms
from rePet.models import Cadastro

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