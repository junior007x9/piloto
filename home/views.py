# views.py
from django.shortcuts import render

# Página inicial que usa o template base
def index(request):
    return render(request, 'base.html')

# views.py
from django.shortcuts import render

# Página que exibe um item específico
def exibir_item(request, id):
    return render(request, 'id.html', {
        'id': id  # Passa o ID como variável para o template
    })

# Página que exibe o dia da semana
def dia_semana(request, dia):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia_nome = dias_semana.get(dia, "Dia inválido")
    return render(request, 'dia_semana.html', {
        'dia': dia,          # Passa o número do dia
        'dia_nome': dia_nome # Passa o nome do dia da semana
    })
