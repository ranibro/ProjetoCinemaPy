from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=32)
    sobrenome = models.CharField('Sobrenome', max_length=32)
    email = models.EmailField('Email', max_length=32)

    def __str__(self):
        return "{}".format(self.nome)

class Sala(models.Model):
    ASSENTOS_CHOICES = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
        ('8', '9'), ('9', '9'), ('10', '10')
    )
    assentos = models.CharField(max_length=8, choices=ASSENTOS_CHOICES)

class Cartaz(models.Model):
    dataCartaz = models.DateTimeField(verbose_name='Data do Cartaz')

    def __str__(self):
        return "Dia {} ás {}".format(self.dataCartaz.strftime('%d/%m/%Y'), self.dataCartaz.strftime('%H:%M'))


class Filme(models.Model):
    CATEGORIA_CHOICES = (
        ('Action', 'Ação'), ('Adventure', 'Aventura'), ('Comedy', 'Comédia'), ('Terror', 'Terror'), ('Drama', 'Drama'),
        ('Fantasy', 'Fantasia'), ('Sci-Fi', 'Ficção'), ('Romance', 'Romance')
    )

    CLASSIFICACAO_CHOICES = (
        ('Livre', 'Livre'), ('10', '10+'), ('12', '12+'), ('14', '14+'),
        ('16', '16+'), ('18', '18+')
    )

    cartaz = models.OneToOneField(Cartaz, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=16)
    sinopse = models.CharField('Sinopse', max_length=128)
    categoria = models.CharField(max_length=32, choices=CATEGORIA_CHOICES)
    classificacao = models.CharField(max_length=32, choices=CLASSIFICACAO_CHOICES)
    duracao = models.CharField('Duração', max_length=16)
    capa = StdImageField('Capa do Filme', upload_to='imagens', variations={'thumb': (90, 90)})

    def __str__(self):
        return "{}".format(self.nome)


class Recibo(models.Model):
    assento = models.IntegerField()
    preco = models.DecimalField(max_digits=16, decimal_places=2)


class Combo(models.Model):
    produto = models.CharField('Produto', max_length=16)
    preco = models.DecimalField(max_digits=16, decimal_places=2)
