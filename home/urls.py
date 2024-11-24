
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),                         # Página inicial
    path('exibir_item/<int:id>/', views.exibir_item, name="exibir_item"),  # Exibir item específico
    path('dia_semana/<int:dia>/', views.dia_semana, name="dia_semana"),# Exibir dia da semana
    path('produtos/', views.produtos, name='produtos'),   
    path('produtos/fomulario_contato/', views.contato, name='fomulario'),
    path('produtos/fomulario_produto/', views.produto, name='fomulario2'), 
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),     
    path('produtos/ver/<int:id>/', views.ver_detalhes, name='ver_detalhes'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
]
