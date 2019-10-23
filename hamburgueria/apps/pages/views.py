from django.shortcuts import render
from django.views.generic import TemplateView
from apps.adicionais.models import Adicional
from apps.ingredientes.models import Ingrediente
# Create your views here.

#views baseadas em classess

class HomePage(TemplateView):
    template_name = 'pages/indexAdm.html'

#views baseadas em funções

def Home(request):
    return render(request, 'pages/indexAdm.html')

def listarAdicionaisAndIngredientes(request):
    adicionais = Adicional.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'pages/estoque/estoque.html', {'adicionais':adicionais, 'ingredientes': ingredientes})

#def Estoque(request):
#    return render(request, 'pages/estoque/estoque.html')