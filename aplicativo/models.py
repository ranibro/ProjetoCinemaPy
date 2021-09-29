from django.db import models
from stdimage import StdImageField


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=32)
    login = models.CharField('Login', max_length=16)
    email = models.CharField('Email', max_length=32)

    def __str__(self):
        return "{}".format(self.nome)

class Cartaz(models.Model):
    dataCartaz = models.DateField(verbose_name='Data do Cartaz')

    def __str__(self):
        return "Cartaz do dia {}".format(self.dataCartaz)

class Filme(models.Model):
    cartaz = models.ForeignKey(Cartaz, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=16)
    sinopse = models.CharField('Sinopse', max_length=128)
    categoria = models.CharField('Categoria', max_length=16)
    classificacao = models.CharField('Classificação', max_length=8)
    duracao = models.CharField('Duração', max_length=16)
    capa = StdImageField('imagem', upload_to='imagens', variations={'thumb': (90, 90)})

    def __str__(self):
        return "{}".format(self.nome)

class Recibo(models.Model):
    assento = models.IntegerField()
    preco = models.DecimalField(max_digits=16, decimal_places=2)
    
class Combo(models.Model):
    produto = models.CharField('Produto', max_length=16)
    preco = models.DecimalField(max_digits=16, decimal_places=2)