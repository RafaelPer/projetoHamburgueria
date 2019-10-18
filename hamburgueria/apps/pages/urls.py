from django.urls import path
from . import views
from apps.adicionais.views import criarAdicional

urlpatterns = [
    path('homepage/', views.Home, name = 'index'),
    path('estoque/', views.Estoque, name = 'estoque'),
    path('estoque/adicionais/novo_adicional', criarAdicional, name = 'novo_adicional')
]