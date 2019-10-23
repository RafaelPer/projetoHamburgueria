from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import IngredienteForm, IngredienteFormReadonly
from .models import Ingrediente
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarIngredientes(ListView):
    model = Ingrediente
    template_name = 'pages/estoque/estoque.html'
    context_object_name = 'ingredientes'
    queryset = Ingrediente.objects.filter(estado = True)

class CriarIngrediente(CreateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'pages/estoque/ingredientes/novo_ingrediente.html'
    success_url = reverse_lazy('estoque')

class EditarIngrediente(UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'pages/estoque/ingredientes/editar_ingrediente.html'
    success_url = reverse_lazy('estoque')

class EliminarIngrediente(DeleteView):
    model = Ingrediente

    def post(self, request, idIngrediente, *args, **kwargs):
        object = Ingrediente.object.get(idIngrediente = idIngrediente)
        object.estado = False
        object.save()
        return redirect('estoque')

#views baseadas em funções

def criarIngrediente(request):
    if request.method == 'POST':
        #nom = request.POST.get('nome')
        #preco = Decimal(request.POST.get('preco'))
        #qtd = Decimal(request.POST.get('quantidade'))
        #un = request.POST.get('unidade')
        #desc = request.POST.get('descricao')
        #print(nom, preco, qtd, un, desc)
        #ingrediente = Ingrediente(nome = nom, descricao = desc, preco = preco, quantidade = qtd, unidade = un)
        #ingrediente.save()
        #return redirect('index')
        #print(request.POST)
        ingrediente_form = IngredienteForm(request.POST)
        if ingrediente_form.is_valid():
            ingrediente_form.save()
            return redirect('estoque')
    else:
        ingrediente_form = IngredienteForm()
    return render(request, 'pages/estoque/ingredientes/novo_ingrediente.html', {'ingrediente_form':ingrediente_form})

def listarIngrediente(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'pages/estoque/estoque.html', {'ingredientes':ingredientes})

def editarIngrediente(request, idIngrediente):
    ingrediente = Ingrediente.objects.get(idIngrediente = idIngrediente)
    print("INGREDIENTE: "+str(ingrediente))
    if request.method == 'GET':
        print("entrou if")
        ingrediente_form = IngredienteForm(instance = ingrediente)
        print("form if: "+str(ingrediente_form))
    else:
        print("entrou else")
        ingrediente_form = IngredienteForm(request.POST, instance = ingrediente)
        print("form else: "+str(ingrediente_form))
        if ingrediente_form.is_valid():
            ingrediente_form.save()
        return redirect('estoque')
    return render(request, 'pages/estoque/ingredientes/editar_ingrediente.html', {'ingrediente_form':ingrediente_form})

def eliminarIngrediente(request, idIngrediente):
    ingrediente = Ingrediente.objects.get(idIngrediente = idIngrediente)
    ingrediente.delete()
    return redirect('estoque')    


def showIngrediente(request, idIngrediente):
    idIngred = idIngrediente
    print("idIngred "+str(idIngred))
    ingrediente = Ingrediente.objects.get(idIngrediente = idIngrediente)
    if request.method == 'GET':
        print("entrou if")
        ingrediente_form = IngredienteFormReadonly(instance = ingrediente)
        print("form if: "+str(ingrediente_form))
    else:
        ingrediente_form = None
    return render(request, 'pages/estoque/ingredientes/mostrar_ingrediente.html', {'ingrediente_form':ingrediente_form, 'idIngrediente': idIngred})