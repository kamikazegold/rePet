from django.db import models

# Create your models here.

class Animal(models.Model):

    animal_tamanho = [
        ('pp', 'Porte Pequeno'),
        ('pm', 'Porte Médio'),
        ('pg', 'Porte Grande'),
    ]

    animal_idade = [
        ('0', 'De 2 a 6 meses'),
        ('1', '1 Ano'),
        ('2', '2 anos'),
        ('3', '3 anos'),
        ('4', '4 anos'),
        ('5', '5 anos'),
        ('6', '6 anos'),
        ('7', '7 anos'),
        ('8', '8 anos'),
    ]
    nome = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=20, choices=animal_tamanho)
    idade = models.CharField(max_length= 20, choices=animal_idade)
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome

class Cadastro(models.Model):

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)