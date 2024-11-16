from django.shortcuts import render

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
    return render(request, 'produtos/lista.html', contexto)

def exibir_item(request, id):
    # Dados simulados
    item = {
        'id': id,
        'nome': 'Item Exemplo',
        'descricao': 'Descrição do item exemplo.',
        'preco': '100,00'
    }
    return render(request, 'produtos/exibir_item.html', {'item': item})

def dia_semana(request, numero):
    dias_da_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
    if 1 <= numero <= 7:
        dia = dias_da_semana[numero - 1]
    else:
        dia = 'Dia inválido'

    contexto = {
        'numero': numero,
        'dia': dia
    }
    return render(request, 'diasemana.html', contexto)

def contato(request):
    return render(request, 'contato.html')

def menu(request):
    return render(request, 'menu.html')

def sobre(request):
    return render(request, 'sobre.html')
