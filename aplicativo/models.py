from django.db import models


class Cliente(models.Model):
    def __str__(self):
        return "{}".format(self.nome)
    nome = models.CharField('Nome', max_length=60)
    login = models.CharField('Login', max_length=60)
    email = models.CharField('Email', max_length=60)

class Agenda(models.Model):
    filmes = models.CharField('Filme', max_length=50)
    cartaz = models.BooleanField()
    dataFilme = models.DateTimeField()

class Filme(models.Model):
    def __str__(self):
        return "{}".format(self.nome)
    nome = models.CharField('Nome', max_length=60)
    sinopse = models.CharField('Sinopse', max_length=300)
    categoria = models.CharField('Categoria', max_length=20)
    classificacao = models.CharField('Classificação', max_length=10)
    duracao = models.CharField('Duração', max_length=30)

class Recibo(models.Model):
    assento = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
class Combo(models.Model):
    produto = models.CharField('Produto', max_length=60)
    preco = models.DecimalField(max_digits=10, decimal_places=2)