from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AdicionalForm, AdicionalFormReadonly
from .models import Adicional
from decimal import Decimal, DecimalException
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

#views baseadas em classes

class ListarAdicionais(ListView):
    model = Adicional
    template_name = 'pages/estoque/estoque.html'
    context_object_name = 'adicionais'
    #queryset = Adicional.objects.filter(estado = True)

class CriarAdicional(CreateView):
    model = Adicional
    form_class = AdicionalForm
    template_name = 'pages/estoque/adicionais/novo_adicional.html'
    success_url = reverse_lazy('estoque')

class EditarAdicional(UpdateView):
    model = Adicional
    form_class = AdicionalForm
    template_name = 'pages/estoque/adicionais/editAdicional.html'
    success_url = reverse_lazy('estoque')

class EliminarAdicional(DeleteView):
    model = Adicional

    def post(self, request, idAdicional, *args, **kwargs):
        object = Adicional.object.get(idAdicional = idAdicional)
        object.estado = False
        object.save()
        return redirect('estoque')

#views baseadas em funções

def criarAdicional(request):
    if request.method == 'POST':
        #nom = request.POST.get('nome')
        #preco = Decimal(request.POST.get('preco'))
        #qtd = Decimal(request.POST.get('quantidade'))
        #un = request.POST.get('unidade')
        #desc = request.POST.get('descricao')
        #print(nom, preco, qtd, un, desc)
        #adicional = Adicional(nome = nom, descricao = desc, preco = preco, quantidade = qtd, unidade = un)
        #adicional.save()
        #return redirect('index')
        #print(request.POST)
        adicional_form = AdicionalForm(request.POST)
        if adicional_form.is_valid():
            adicional_form.save()
            return redirect('estoque')
    else:
        adicional_form = AdicionalForm()
    print(adicional_form)
    return render(request, 'pages/estoque/adicionais/novo_adicional.html', {'adicional_form':adicional_form})

def listarAdicional(request):
    adicionais = Adicional.objects.all()
    return render(request, 'pages/estoque/estoque.html', {'adicionais':adicionais})

def editarAdicional(request, idAdicional):
    adicional = Adicional.objects.get(idAdicional = idAdicional)
    print("ADICIONAL: "+str(adicional))
    if request.method == 'GET':
        print("entrou if")
        adicional_form = AdicionalForm(instance = adicional)
        print("form if: "+str(adicional_form))
    else:
        print("entrou else")
        adicional_form = AdicionalForm(request.POST, instance = adicional)
        print("form else: "+str(adicional_form))
        if adicional_form.is_valid():
            adicional_form.save()
        return redirect('estoque')
    return render(request, 'pages/estoque/adicionais/editAdicional.html', {'adicional_form':adicional_form})

def eliminarAdicional(request, idAdicional):
    adicional = Adicional.objects.get(idAdicional = idAdicional)
    adicional.delete()
    return redirect('estoque')    


def showAdicional(request, idAdicional):
    idAdi = idAdicional
    print("idadi "+str(idAdi))
    adicional = Adicional.objects.get(idAdicional = idAdicional)
    if request.method == 'GET':
        print("entrou if")
        adicional_form = AdicionalFormReadonly(instance = adicional)
        print("form if: "+str(adicional_form))
    else:
        adicional_form = None
    return render(request, 'pages/estoque/adicionais/showAdicional.html', {'adicional_form':adicional_form, 'idAdicional': idAdi})