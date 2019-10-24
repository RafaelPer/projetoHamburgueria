from django.shortcuts import render
from django.views.generic import TemplateView
from apps.adicionais.models import Adicional
from django.http import HttpResponse
import json
from apps.ingredientes.models import Ingrediente
from apps.pais.models import Pais
from apps.estado.models import Estado
from apps.cidade.models import Cidade
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

def get_estado(request, idPais):
    pais = Pais.objects.get(idPais=idPais)
    print(pais)
    estados = Estado.objects.filter(estadoPais=pais)
    print(estados)
    estados_dict = {}
    for estado in estados:
        # if your subcategory has field name
        estados_dict[estado.idEstado] = estado.nome
    print(estados_dict)
    print(json.dumps(estados_dict))
    return HttpResponse(json.dumps(estados_dict), content_type="application/json")

def get_cidade(request, idEstado):
    estado = Estado.objects.get(idEstado=idEstado)
    cidades = Cidade.objects.filter(cidadeEstado=estado)
    cidades_dict = {}
    for cidade in cidades:
        # if your subcategory has field name
        cidades_dict[cidade.idCidade] = cidade.nome
    return HttpResponse(json.dumps(cidades_dict), content_type="application/json")