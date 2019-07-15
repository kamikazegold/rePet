from django.shortcuts import render
from rePet.models import Animal, Cadastro, Usuario
from rePet.forms import CadastroForm, LoginUsuario

# Create your views here.

def mostrar_index(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais': animais})

def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None)
    msg =''

    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm()
        msg = 'cadastro realizado com sucesso'
    
    contexto = {
        'form': formulario,
        'msg': msg
    }
    return render(request, 'cadastro.html', contexto)