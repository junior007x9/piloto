from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>A view index funciona, Wow!</h1>")

def home(request):
    return HttpResponse("<h1>Página Principal</h1>")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim mesmo.</h1>")
