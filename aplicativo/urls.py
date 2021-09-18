from aplicativo.views import index, filmes
from django.urls import path

app_name = 'aplicativo'

urlpatterns = [
    path('', index),
    path('filmes', filmes, name='filmes')
]