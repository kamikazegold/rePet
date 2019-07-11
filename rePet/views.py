from django.shortcuts import render
from rePet.models import Animal

# Create your views here.

def mostrar_index(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais': animais})