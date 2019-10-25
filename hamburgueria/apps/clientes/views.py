from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteForm, ClienteFormReadonly
from .models import Cliente
from apps.pais.models import Pais
from apps.estado.models import Estado
from apps.cidade.models import Cidade
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarCliente(ListView):
    model = Cliente
    template_name = 'pages/pessoas/clientes/clientes.html'
    context_object_name = 'clientes'
    #queryset = Cliente.objects.filter(ativo = 'Sim')

class CriarCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'pages/pessoas/clientes/novo_cliente.html'
    success_url = reverse_lazy('clientes')

class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'pages/pessoas/clientes/editar_cliente.html'
    success_url = reverse_lazy('clientes')

class EliminarCliente(DeleteView):
    model = Cliente

    def post(self, request, idCliente, *args, **kwargs):
        object = Cliente.object.get(idCliente = idCliente)
        object.ativo = 'Não'
        object.save()
        return redirect('clientes')

#views baseadas em funções

def criarCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILES)
        if cliente_form.is_valid():
            print(cliente_form.save())
            cliente_form.save()
            return redirect('clientes')
    else:
        cliente_form = ClienteForm()
    print("Cliente: "+str(cliente_form))
    pais = Pais.objects.all()
    return render(request, 'pages/pessoas/clientes/novo_cliente.html', {'cliente_form':cliente_form, 'pais':pais})

def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'pages/pessoas/clientes/clientes.html', {'clientes':clientes})

def editarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente = idCliente)
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("Cliente: "+str(cliente))
    if request.method == 'GET':
        print("entrou if")
        cliente_form = ClienteForm(instance = cliente)
        print("form if: "+str(cliente_form))
    else:
        print("entrou else")
        cliente_form = ClienteForm(request.POST, request.FILES, instance = cliente)
        print("form else: "+str(cliente_form))
        if cliente_form.is_valid():
            cliente_form.save()
            print("form is valid ")
        else: 
            print("form is invalid ")
        return redirect('clientes')
    return render(request, 'pages/pessoas/clientes/editar_cliente.html', {'cliente_form':cliente_form, 'paises':paises, 'estados': estados, 'cidades': cidades})

def eliminarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente = idCliente)
    cliente.delete()
    return redirect('clientes')    


def showCliente(request, idCliente):
    idCli = idCliente
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("idCli "+str(idCli))
    cliente = Cliente.objects.get(idCliente = idCliente)
    if request.method == 'GET':
        print("entrou if")
        cliente_form = ClienteFormReadonly(instance = cliente)
        print("form if: "+str(cliente_form))
    else:
        cliente_form = None
    return render(request, 'pages/pessoas/clientes/show_cliente.html', {'cliente_form':cliente_form, 'idCliente': idCli, 'paises':paises, 'estados': estados, 'cidades': cidades})