from django.shortcuts import render, redirect, resolve_url
from django.core.exceptions import ObjectDoesNotExist
from .forms import LancheForm, LancheFormReadonly, LancheIngredientesForm
from .models import Lanche, LancheIngredientes
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import ListView,   DetailView, UpdateView, CreateView, DeleteView

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
    lanche_formu = Lanche()
    inglediente_lanche_formset = inlineformset_factory(
        Lanche,
        LancheIngredientes,
        form=LancheIngredientesForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        lanche_form = LancheForm(request.POST, request.FILES, instance=lanche_formu)
        formset = inglediente_lanche_formset(
            request.POST,
            instance=lanche_formu, 
            prefix='lanche'
        )
        if lanche_form.is_valid() and formset.is_valid():
            print(lanche_form.save())
            lanche_form.save()
            formset.save()
            return redirect('lanches')
    else:
        lanche_form = LancheForm()
        formset = inglediente_lanche_formset(instance=lanche_formu, prefix='lanche')
    print("lanche: "+str(lanche_form))
    return render(request, 'pages/lanchesAndBebidas/lanches/novo_lanche.html', {'lanche_form':lanche_form, 'formset':formset})

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
        lanche_form = LancheForm(request.POST, request.FILES, request.FILES, instance = lanche)
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