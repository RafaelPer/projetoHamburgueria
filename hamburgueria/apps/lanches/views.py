from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import LancheForm, LancheFormReadonly
from .models import Lanche
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarLanches(ListView):
    model = Lanche
    template_name = 'pages/lanchesAndBebidas/lanches/lanches.html'
    context_object_name = 'Lanches'
    #queryset = Lanche.objects.filter(estado = True)

class CriarLanche(CreateView):
    model = Lanche
    form_class = LancheForm
    template_name = 'pages/lanchesAndBebidas/lanches/novo_lanche.html'
    success_url = reverse_lazy('lanches')

class EditarLanche(UpdateView):
    model = Lanche
    form_class = LancheForm
    template_name = 'pages/lanchesAndBebidas/lanches/editar_lanche.html'
    success_url = reverse_lazy('lanches')

class EliminarLanche(DeleteView):
    model = Lanche

    def post(self, request, idLanche, *args, **kwargs):
        object = Lanche.object.get(idLanche = idLanche)
        object.estado = True
        object.save()
        return redirect('lanches')

#views baseadas em funções

def criarLanche(request):
    if request.method == 'POST':
        lanche_form = LancheForm(request.POST)
        if lanche_form.is_valid():
            print(lanche_form.save())
            lanche_form.save()
            return redirect('lanches')
    else:
        lanche_form = LancheForm()
    print("lanche: "+str(lanche_form))
    return render(request, 'pages/lanchesAndBebidas/lanches/novo_lanche.html', {'lanche_form':lanche_form})

def listarLanches(request):
    lanches = Lanche.objects.all()
    return render(request, 'pages/lanchesAndBebidas/lanches/lanches.html', {'lanches':lanches})

def editarLanche(request, idLanche):
    lanche = Lanche.objects.get(idLanche = idLanche)
    print("lanche: "+str(lanche))
    if request.method == 'GET':
        print("entrou if")
        lanche_form = LancheForm(instance = lanche)
        print("form if: "+str(lanche_form))
    else:
        print("entrou else")
        lanche_form = LancheForm(request.POST, instance = lanche)
        print("form else: "+str(lanche_form))
        if lanche_form.is_valid():
            lanche_form.save()
            print("form is valid ")
        else: 
            print("form is invalid ")
        return redirect('lanches')
    return render(request, 'pages/lanchesAndBebidas/lanches/editar_lanche.html', {'lanche_form':lanche_form})

def eliminarLanche(request, idLanche):
    lanche = Lanche.objects.get(idLanche = idLanche)
    lanche.delete()
    return redirect('lanches')    


def showLanche(request, idLanche):
    idLanch = idLanche
    print("idTipoFunc "+str(idLanch))
    lanche = Lanche.objects.get(idLanche = idLanche)
    if request.method == 'GET':
        print("entrou if")
        lanche_form = LancheFormReadonly(instance = lanche)
        print("form if: "+str(lanche_form))
    else:
        lanche_form = None
    return render(request, 'pages/lanchesAndBebidas/lanches/show_lanche.html', {'lanche_form':lanche_form, 'idLanche': idLanch})