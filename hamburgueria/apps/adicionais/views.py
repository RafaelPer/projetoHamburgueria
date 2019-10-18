from django.shortcuts import render, redirect
from .forms import AdicionalForm

# Create your views here.
def criarAdicional(request):
    if request.method == 'POST':
        auto_form = AdicionalForm(request.POST)
        if auto_form.is_valid():
            auto_form.save()
            return redirect('index')
    else:
        auto_form = AdicionalForm()
    return render(request, 'pages/estoque/adicionais/novo_adicional.html', {'auto_form': auto_form})