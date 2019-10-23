from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FornecedorForm, FornecedorFormReadonly
from .models import Fornecedor
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarFornecedor(ListView):
    model = Fornecedor
    template_name = 'pages/estoque/fornecedores/fornecedores.html'
    context_object_name = 'ingredientes'
    queryset = Fornecedor.objects.filter(ativo = 'Sim')

class CriarFornecedor(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'pages/estoque/fornecedores/novo_fornecedor.html'
    success_url = reverse_lazy('fornecedores')

class EditarFornecedor(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'pages/estoque/fornecedores/editar_fornecedor.html'
    success_url = reverse_lazy('fornecedores')

class EliminarFornecedor(DeleteView):
    model = Fornecedor

    def post(self, request, idFornecedor, *args, **kwargs):
        object = Fornecedor.object.get(idFornecedor = idFornecedor)
        object.ativo = 'Não'
        object.save()
        return redirect('fornecedores')

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