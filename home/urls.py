from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
]
