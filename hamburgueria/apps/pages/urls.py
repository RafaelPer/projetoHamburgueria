from django.urls import path
from . import views
from apps.adicionais.views import criarAdicional, showAdicional, editarAdicional, eliminarAdicional
from apps.ingredientes.views import criarIngrediente, showIngrediente, editarIngrediente, eliminarIngrediente

urlpatterns = [
    path('homepage/', views.Home, name = 'index'),

    #estoque
    #path('estoque/', ListarAdicionais.as_view(), name = 'estoque'),
    path('estoque/', views.listarAdicionaisAndIngredientes, name = 'estoque'),

    #adicional
    path('estoque/adicionais/novo_adicional', criarAdicional, name = 'novo_adicional'),
    path('estoque/adicionais/editar_adicional/<int:idAdicional>', editarAdicional, name = 'editar_adicional'),
    path('estoque/adicionais/mostrar_adicional/<int:idAdicional>', showAdicional, name = 'show_adicional'),
    path('estoque/adicionais/eliminar_adicional/<int:idAdicional>', eliminarAdicional, name = 'eliminar_adicional'),

    #ingredientes
    path('estoque/ingredientes/novo_ingrediente', criarIngrediente, name = 'novo_ingrediente'),
    path('estoque/ingredientes/editar_ingrediente/<int:idIngrediente>', editarIngrediente, name = 'editar_ingrediente'),
    path('estoque/ingredientes/mostrar_ingrediente/<int:idIngrediente>', showIngrediente, name = 'show_ingrediente'),
    path('estoque/ingredientes/eliminar_ingrediente/<int:idIngrediente>', eliminarIngrediente, name = 'eliminar_ingrediente'),

    #fornecedores
    path('estoque/', views.listarFornecedores, name = 'estoque'),
    path('estoque/fornecedores/novo_fornecedor', criarFornecedor, name = 'novo_fornecedor'),
    path('estoque/fornecedores/editar_fornecedor/<int:idFornecedor>', editarFornecedor, name = 'editar_fornecedor'),
    path('estoque/fornecedores/mostrar_fornecedor/<int:idFornecedor>', showFornecedor, name = 'show_fornecedor'),
    path('estoque/fornecedores/eliminar_fornecedor/<int:idFornecedor>', eliminarFornecedor, name = 'eliminar_fornecedor'),
    
]