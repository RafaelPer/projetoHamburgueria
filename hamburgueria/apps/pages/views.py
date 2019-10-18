from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'pages/indexAdm.html')

def Estoque(request):
    return render(request, 'pages/estoque/estoque.html')