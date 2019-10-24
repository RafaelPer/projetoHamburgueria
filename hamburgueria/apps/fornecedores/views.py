from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FornecedorForm, FornecedorFormReadonly
from .models import Fornecedor
from apps.pais.models import Pais
from apps.estado.models import Estado
from apps.cidade.models import Cidade
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarFornecedor(ListView):
    model = Fornecedor
    template_name = 'pages/estoque/fornecedores/fornecedores.html'
    context_object_name = 'fornecedores'
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

def criarFornecedor(request):
    if request.method == 'POST':
        fornecedor_form = FornecedorForm(request.POST, request.FILES)
        if fornecedor_form.is_valid():
            print(fornecedor_form.save())
            fornecedor_form.save()
            return redirect('fornecedores')
    else:
        fornecedor_form = FornecedorForm()
    print("FORNECEDOR: "+str(fornecedor_form))
    pais = Pais.objects.all()
    return render(request, 'pages/estoque/fornecedores/novo_fornecedor.html', {'fornecedor_form':fornecedor_form, 'pais':pais})

def listarFornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'pages/estoque/fornecedores/fornecedores.html', {'fornecedores':fornecedores})

def editarFornecedor(request, idFornecedor):
    fornecedor = Fornecedor.objects.get(idFornecedor = idFornecedor)
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("FORNECEDOR: "+str(fornecedor))
    if request.method == 'GET':
        print("entrou if")
        fornecedor_form = FornecedorForm(instance = fornecedor)
        print("form if: "+str(fornecedor_form))
    else:
        print("entrou else")
        fornecedor_form = FornecedorForm(request.POST, request.FILES, instance = fornecedor)
        print("form else: "+str(fornecedor_form))
        if fornecedor_form.is_valid():
            fornecedor_form.save()
        return redirect('fornecedores')
    return render(request, 'pages/estoque/fornecedores/editar_fornecedor.html', {'fornecedor_form':fornecedor_form, 'paises':paises, 'estados': estados, 'cidades': cidades})

def eliminarFornecedor(request, idFornecedor):
    fornecedor = Fornecedor.objects.get(idFornecedor = idFornecedor)
    fornecedor.delete()
    return redirect('fornecedores')    


def showFornecedor(request, idFornecedor):
    idForn = idFornecedor
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("idForn "+str(idForn))
    fornecedor = Fornecedor.objects.get(idFornecedor = idFornecedor)
    if request.method == 'GET':
        print("entrou if")
        fornecedor_form = FornecedorFormReadonly(instance = fornecedor)
        print("form if: "+str(fornecedor_form))
    else:
        fornecedor_form = None
    return render(request, 'pages/estoque/fornecedores/show_fornecedor.html', {'fornecedor_form':fornecedor_form, 'idFornecedor': idForn, 'paises':paises, 'estados': estados, 'cidades': cidades})