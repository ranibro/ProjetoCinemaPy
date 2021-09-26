from django import forms
from GerenciaCinema import settings
from aplicativo.models import Filme, Cliente, Cartaz, Recibo, Combo

class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['cartaz', 'nome', 'sinopse', 'categoria', 'classificacao', 'duracao', 'capa']


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'login', 'email']

class CartazModelForm(forms.ModelForm):
    class Meta:
        model = Cartaz
        fields = ['dataCartaz']
        widgets = {
            'dataCartaz': forms.DateInput(format=settings.DATE_INPUT_FORMATS,
                                          attrs={'placeholder': 'Ex:. 01/01/2000'})
        }
