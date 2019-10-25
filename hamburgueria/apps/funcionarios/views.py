from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FuncionarioForm, FuncionarioFormReadonly
from .models import Funcionario
from apps.pais.models import Pais
from apps.estado.models import Estado
from apps.cidade.models import Cidade
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarFuncionarios(ListView):
    model = Funcionario
    template_name = 'pages/pessoas/pessoas.html'
    context_object_name = 'funcionarios'
    #queryset = Funcionario.objects.filter(ativo = 'Sim')

class CriarFuncionario(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'pages/pessoas/funcionarios/novo_funcionario.html'
    success_url = reverse_lazy('funcionarios')

class EditarFuncionario(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'pages/pessoas/funcionarios/editar_funcionario.html'
    success_url = reverse_lazy('funcionarios')

class EliminarFuncionario(DeleteView):
    model = Funcionario

    def post(self, request, idFuncionario, *args, **kwargs):
        object = Funcionario.object.get(idFuncionario = idFuncionario)
        object.ativo = 'Não'
        object.save()
        return redirect('funcionarios')

#views baseadas em funções

def criarFuncionario(request):
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST, request.FILES)
        if funcionario_form.is_valid():
            print(funcionario_form.save())
            funcionario_form.save()
            return redirect('funcionarios')
    else:
        funcionario_form = FuncionarioForm()
    print("funcionario: "+str(funcionario_form))
    pais = Pais.objects.all()
    return render(request, 'pages/pessoas/funcionarios/novo_funcionario.html', {'funcionario_form':funcionario_form, 'pais':pais})

def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'pages/pessoas/pessoas.html', {'funcionarios':funcionarios})

def editarFuncionario(request, idFuncionario):
    funcionario = Funcionario.objects.get(idFuncionario = idFuncionario)
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("funcionario: "+str(funcionario))
    if request.method == 'GET':
        print("entrou if")
        funcionario_form = FuncionarioForm(instance = funcionario)
        print("form if: "+str(funcionario_form))
    else:
        print("entrou else")
        funcionario_form = FuncionarioForm(request.POST, request.FILES, instance = funcionario)
        print("form else: "+str(funcionario_form))
        if funcionario_form.is_valid():
            funcionario_form.save()
            print("form is valid ")
        else: 
            print("form is invalid ")
        return redirect('funcionarios')
    return render(request, 'pages/pessoas/funcionarios/editar_funcionario.html', {'funcionario_form':funcionario_form, 'paises':paises, 'estados': estados, 'cidades': cidades})

def eliminarFuncionario(request, idFuncionario):
    funcionario = Funcionario.objects.get(idFuncionario = idFuncionario)
    funcionario.delete()
    return redirect('funcionarios')    


def showFuncionario(request, idFuncionario):
    idFunc = idFuncionario
    paises = Pais.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    print("idFunc "+str(idFunc))
    funcionario = Funcionario.objects.get(idFuncionario = idFuncionario)
    if request.method == 'GET':
        print("entrou if")
        funcionario_form = FuncionarioFormReadonly(instance = funcionario)
        print("form if: "+str(funcionario_form))
    else:
        funcionario_form = None
    return render(request, 'pages/pessoas/funcionarios/show_funcionario.html', {'funcionario_form':funcionario_form, 'idFuncionario': idFunc, 'paises':paises, 'estados': estados, 'cidades': cidades})