from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import TipoFuncionarioForm, TipoFuncionarioFormReadonly
from .models import tipoFuncionario
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarTiposFuncionarios(ListView):
    model = tipoFuncionario
    template_name = 'pages/pessoas/funcionarios/tipoFuncionario/tipofuncionario.html'
    context_object_name = 'tipoFuncionarios'
    #queryset = tipoFuncionario.objects.filter(estado = True)

class CriarTipoFuncionario(CreateView):
    model = tipoFuncionario
    form_class = TipoFuncionarioForm
    template_name = 'pages/pessoas/funcionarios/tipoFuncionario/novo_tipofuncionario.html'
    success_url = reverse_lazy('tipoFuncionario')

class EditarTipoFuncionario(UpdateView):
    model = tipoFuncionario
    form_class = TipoFuncionarioForm
    template_name = 'pages/pessoas/funcionarios/tipoFuncionario/editar_tipofuncionario.html'
    success_url = reverse_lazy('tipoFuncionario')

class EliminarTipoFuncionario(DeleteView):
    model = tipoFuncionario

    def post(self, request, idTipoFuncionario, *args, **kwargs):
        object = tipoFuncionario.object.get(idTipoFuncionario = idTipoFuncionario)
        object.estado = True
        object.save()
        return redirect('tipoFuncionario')

#views baseadas em funções

def criarTipoFuncionario(request):
    if request.method == 'POST':
        tipofuncionario_form = TipoFuncionarioForm(request.POST)
        if tipofuncionario_form.is_valid():
            print(tipofuncionario_form.save())
            tipofuncionario_form.save()
            return redirect('tipoFuncionario')
    else:
        tipofuncionario_form = TipoFuncionarioForm()
    print("funcionario: "+str(tipofuncionario_form))
    return render(request, 'pages/pessoas/funcionarios/tipoFuncionario/novo_tipofuncionario.html', {'tipofuncionario_form':tipofuncionario_form})

def listarTiposFuncionarios(request):
    tiposfuncionarios = tipoFuncionario.objects.all()
    return render(request, 'pages/pessoas/funcionarios/tipoFuncionario/tipofuncionario.html', {'tiposfuncionarios':tiposfuncionarios})

def editarTipoFuncionario(request, idTipoFuncionario):
    tipofuncionario = tipoFuncionario.objects.get(idTipoFuncionario = idTipoFuncionario)
    print("tipofuncionario: "+str(tipofuncionario))
    if request.method == 'GET':
        print("entrou if")
        tipofuncionario_form = TipoFuncionarioForm(instance = tipofuncionario)
        print("form if: "+str(tipofuncionario_form))
    else:
        print("entrou else")
        tipofuncionario_form = TipoFuncionarioForm(request.POST, instance = tipofuncionario)
        print("form else: "+str(tipofuncionario_form))
        if tipofuncionario_form.is_valid():
            tipofuncionario_form.save()
            print("form is valid ")
        else: 
            print("form is invalid ")
        return redirect('tipoFuncionario')
    return render(request, 'pages/pessoas/funcionarios/tipoFuncionario/editar_tipofuncionario.html', {'tipofuncionario_form':tipofuncionario_form})

def eliminarTipoFuncionario(request, idTipoFuncionario):
    tipofuncionario = tipoFuncionario.objects.get(idTipoFuncionario = idTipoFuncionario)
    tipofuncionario.delete()
    return redirect('tipoFuncionario')    


def showTipoFuncionario(request, idTipoFuncionario):
    idTipoFunc = idTipoFuncionario
    print("idTipoFunc "+str(idTipoFunc))
    tipofuncionario = tipoFuncionario.objects.get(idTipoFuncionario = idTipoFuncionario)
    if request.method == 'GET':
        print("entrou if")
        tipofuncionario_form = TipoFuncionarioFormReadonly(instance = tipofuncionario)
        print("form if: "+str(tipofuncionario_form))
    else:
        tipofuncionario_form = None
    return render(request, 'pages/pessoas/funcionarios/tipoFuncionario/show_tipofuncionario.html', {'tipofuncionario_form':tipofuncionario_form, 'idTipoFuncionario': idTipoFunc})