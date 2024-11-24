# views.py
from django.shortcuts import render
#forms.py
from .forms import ContatoForm
from .forms import FormProduto
from .forms import ProdutoForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Página inicial que usa o template base
def index(request):
    return render(request, 'base.html')

# views.py
from django.shortcuts import render

# Página que exibe um item específico
def exibir_item(request, id):
    if request.method == 'POST':
        id = request.POST.get('id')  # Obtém o ID do item enviado pelo formulário


    return render(request, 'id.html', {
        'id': id,  # Passa o ID como variável para o template
        
        
    })

# Página que exibe o dia da semana
def dia_semana(request, dia):
    dia_nome = ''
    dia = None

    if request.method == 'POST':
        dia = int(request.POST.get('dia'))

        # Mapeia o número para o nome do dia da semana
        dias_da_semana = {
            1: 'Domingo',
            2: 'Segunda-feira',
            3: 'Terça-feira',
            4: 'Quarta-feira',
            5: 'Quinta-feira',
            6: 'Sexta-feira',
            7: 'Sábado',
        }

        dia_nome = dias_da_semana.get(dia, 'Número inválido')

    return render(request, 'dia_semana.html', {
        'dia': dia,          # Passa o número do dia
        'dia_nome': dia_nome # Passa o nome do dia da semana
    })
produtos_lista = [
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
]
    
def produtos(request):
    contexto = {
        'lista': produtos_lista,  
    }
    return render(request, 'produto/lista.html', contexto)

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/formulario.html', contexto)


def produto(request):
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            # Adiciona o novo produto à lista
            novo_produto = {
                'id': len(produtos_lista) + 1,  # Gera um novo ID
                'nome': form.cleaned_data['nome'],
                'preco': form.cleaned_data['preco'],
            }
            produtos_lista.append(novo_produto)  # Adiciona o produto à lista
            return redirect('produtos') # Redireciona para a lista de produtos tem que importa from django.shortcuts import render, redirect
    else:
        form = FormProduto()

    contexto = {
        'form': form,
    }
    return render(request, 'produto/forms_produto.html', contexto)

def excluir_produto(request, id):
    # Verifica se o produto existe na lista
    produto = next((p for p in produtos_lista if p['id'] == id), None)
    
    if produto:
        produtos_lista.remove(produto)  # Remove o produto da lista
    return redirect('produtos')  # Redireciona para a lista de produtos

# View para ver os detalhes de um produto
def ver_detalhes(request, id):
    # Lógica para buscar o produto pelo ID
    produto = next((p for p in produtos_lista if p['id'] == id), None)
    return render(request, 'produto/detalhes.html', {'produto': produto})

# View para editar um produto
def editar_produto(request, id):
    # Lógica para edição do produto
    produto = next((p for p in produtos_lista if p['id'] == id), None)
    if not produto:
        return HttpResponse("Produto não encontrado", status=404)
    
    
    
    if request.method == 'POST':
        # Atualiza os dados do formulário
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Aqui, você atualizaria o produto no banco de dados
            produto['nome'] = form.cleaned_data['nome']
            produto['preco'] = form.cleaned_data['preco']
            return redirect('produtos')
    else:
        # Preenche o formulário com os dados do produto
        form = ProdutoForm(initial={'nome': produto['nome'], 'preco': produto['preco']})

    return render(request, 'produto/editar.html', {'form': form})
