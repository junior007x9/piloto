from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def exibir_item(request, id):
    return render(request, 'item.html', {'id': id})
