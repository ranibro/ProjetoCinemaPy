from django import forms
from GerenciaCinema import settings
from aplicativo.models import Filme, Cliente, Agenda, Recibo, Combo

class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'sinopse', 'categoria', 'classificacao', 'duracao']

        duracao = forms.DateTimeField(widget=forms.DateTimeInput(format='%H:%M:%S'),
                                      input_formats='%H:%M:%S')

        # widget vai mostrar como texto de fundo a formatação de data
        # que o sistema aceita para o usuário visualizar
        # o formato de data está localizado em settings.py

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'login', 'email']