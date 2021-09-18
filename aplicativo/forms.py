from django import forms
from aplicativo.models import Filme, Cliente, Agenda, Recibo, Combo

class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'sinopse', 'categoria', 'classificacao', 'duracao']

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'login', 'email']
