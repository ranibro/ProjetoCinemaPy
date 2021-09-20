from aplicativo.views import index, filmes, cliente
from django.urls import path

app_name = 'aplicativo'

urlpatterns = [
    path('', index),
    path('filmes', filmes, name='filmes'),
    path('cliente', cliente, name='cliente')
]