from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a view 'index'
    path('home/', views.home, name='home'),  # Rota para a view 'home'
    path('sobre/', views.sobre, name='sobre'),  # Rota para a view 'sobre'
]
