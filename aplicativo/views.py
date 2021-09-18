from django.shortcuts import render
from django.contrib import messages
from aplicativo.forms import FilmesModelForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def filmes(request):
    if request.method == 'POST':
        form = FilmesModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme registrado com sucesso!')
            form = FilmesModelForm()
        else:
            messages.error(request, 'Filme não registrado!')
    else:
        form = FilmesModelForm()
    context = {
        'form': form
    }
    return render(request, 'filmes.html', context)