from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('exibir_item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('menu/', views.menu, name='menu'),
    path('sobre/', views.sobre, name='sobre'),
    path('produtos/', views.produtos, name='produtos'),
    path('dia_semana/<int:numero>/', views.dia_semana, name='dia_semana'),  # Adicionada nova URL
]
