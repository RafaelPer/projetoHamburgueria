from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import BebidaForm, BebidaFormReadonly
from .models import Bebida
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarBebidas(ListView):
    model = Bebida
    template_name = 'pages/lanchesAndBebidas/bebidas/bebidas.html'
    context_object_name = 'Bebidas'
    #queryset = Lanche.objects.filter(estado = True)

class CriarBebida(CreateView):
    model = Bebida
    form_class = BebidaForm
    template_name = 'pages/lanchesAndBebidas/bebidas/novo_bebida.html'
    success_url = reverse_lazy('bebidas')

class EditarBebida(UpdateView):
    model = Bebida
    form_class = BebidaForm
    template_name = 'pages/lanchesAndBebidas/bebidas/editar_bebida.html'
    success_url = reverse_lazy('bebidas')

class EliminarBebida(DeleteView):
    model = Bebida

    def post(self, request, idBebida, *args, **kwargs):
        object = Bebida.object.get(idBebida = idBebida)
        object.estado = True
        object.save()
        return redirect('bebidas')

#views baseadas em funções

def criarBebida(request):
    if request.method == 'POST':
        bebida_form = BebidaForm(request.POST, request.FILES)
        if bebida_form.is_valid():
            print(bebida_form.save())
            bebida_form.save()
            return redirect('bebidas')
        else:
            print("is invalid form")
    else:
        bebida_form = BebidaForm()
    print("bebida: "+str(bebida_form))
    return render(request, 'pages/lanchesAndBebidas/bebidas/novo_bebida.html', {'bebida_form':bebida_form})

def listarBebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, 'pages/lanchesAndBebidas/bebidas/bebidas.html', {'bebidas':bebidas})

def editarBebida(request, idBebida):
    bebida = Bebida.objects.get(idBebida = idBebida)
    print("bebida: "+str(bebida))
    if request.method == 'GET':
        print("entrou if")
        bebida_form = BebidaForm(instance = bebida)
        print("form if: "+str(bebida_form))
    else:
        print("entrou else")
        bebida_form = BebidaForm(request.POST, request.FILES, request.FILES, instance = bebida)
        print("form else: "+str(bebida_form))
        if bebida_form.is_valid():
            bebida_form.save()
            print("form is valid ")
        else: 
            print("form is invalid ")
        return redirect('bebidas')
    return render(request, 'pages/lanchesAndBebidas/bebidas/editar_bebida.html', {'bebida_form':bebida_form})

def eliminarBebida(request, idBebida):
    bebida = Bebida.objects.get(idBebida = idBebida)
    bebida.delete()
    return redirect('bebidas')    


def showBebida(request, idBebida):
    idBeb = idBebida
    print("idBeb "+str(idBeb))
    bebida = Bebida.objects.get(idBebida = idBebida)
    if request.method == 'GET':
        print("entrou if")
        bebida_form = BebidaFormReadonly(instance = bebida)
        print("form if: "+str(bebida_form))
    else:
        bebida_form = None
    return render(request, 'pages/lanchesAndBebidas/bebidas/show_bebida.html', {'bebida_form':bebida_form, 'idBebida': idBeb})