from django.shortcuts import render, get_object_or_404
from .models import Item

def index(request):
    return render(request, 'index.html')
def home(request):
    context = {
        'username': 'carlos',
        'items': ['lapis', 'caneta', 'borracha']
    }
    return render(request, 'home.html', context)
def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html',contexto)

def produtos(request):
    return render(request, 'produtos/lista.html')


def exibir_item(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'produtos/exibir_item.html', {'item': item})


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
    return render(request, 'produtos/lista.html')
