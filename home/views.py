from django.shortcuts import render
from .models import Item

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def exibir_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'exibir_item.html', {'id': item.id})

def menu(request):
    return render(request, 'menu.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    return render(request, 'produtos.html')
