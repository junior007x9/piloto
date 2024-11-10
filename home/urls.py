# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),                         # Página inicial
    path('exibir_item/<int:id>/', views.exibir_item, name="exibir_item"),  # Exibir item específico
    path('dia_semana/<int:dia>/', views.dia_semana, name="dia_semana"),    # Exibir dia da semana
]
