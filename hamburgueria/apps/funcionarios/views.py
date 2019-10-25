from django.shortcuts import render
from .models import Funcionario

# Create your views here.


def listarFuncionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'pages/pessoas/pessoas.html', {'funcionarios':funcionarios})