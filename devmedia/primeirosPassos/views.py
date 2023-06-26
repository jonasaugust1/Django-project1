from django.shortcuts import render
from .models import Pessoa

def listar_registros(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoa': pessoa})
