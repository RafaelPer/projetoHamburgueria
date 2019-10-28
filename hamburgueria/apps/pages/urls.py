from django.urls import path
from . import views
from apps.adicionais.views import criarAdicional, showAdicional, editarAdicional, eliminarAdicional
from apps.ingredientes.views import criarIngrediente, showIngrediente, editarIngrediente, eliminarIngrediente
from apps.fornecedores.views import criarFornecedor, showFornecedor, listarFornecedores, editarFornecedor, eliminarFornecedor
from apps.clientes.views import criarCliente, showCliente, listarClientes, editarCliente, eliminarCliente
from apps.funcionarios.views import  criarFuncionario, showFuncionario, listarFuncionarios, editarFuncionario, eliminarFuncionario
from apps.tipoFuncionario.views import  criarTipoFuncionario, showTipoFuncionario, listarTiposFuncionarios, editarTipoFuncionario, eliminarTipoFuncionario
from apps.lanches.views import criarLanche, showLanche, listarLanches, editarLanche, eliminarLanche
#from apps.bebidas.views import criarBebida, showBebida, listarBebidas, editarBebida, eliminarBebida

urlpatterns = [
    path('homepage/', views.Home, name = 'index'),

    #estoque e pessoas
    #path('estoque/', ListarAdicionais.as_view(), name = 'estoque'),
    path('estoque/', views.listarAdicionaisAndIngredientes, name = 'estoque'),
    path('pessoas/', listarFuncionarios, name = 'pessoas'),

    #get estado e cidade fornecedores
    path('estoque/fornecedores/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('estoque/fornecedores/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

    #get estado e cidade listclientes
    path('pessoas/clientes/listclientes/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('pessoas/clientes/listclientes/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

    #get estado e cidade pessoas
    path('pessoas/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('pessoas/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

    #get estado e cidade fornecedores/editar_fornecedor
    path('estoque/fornecedores/editar_fornecedor/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('estoque/fornecedores/editar_fornecedor/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

    #get estado e cidade clientes/listclientes/editar_cliente/
    path('pessoas/clientes/listclientes/editar_cliente/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('pessoas/clientes/listclientes/editar_cliente/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

    #get estado e cidade pessoas/editar_funcionario/
    path('pessoas/editar_funcionario/get-estado/<int:idPais>',views.get_estado, name='get_estado'),
    path('pessoas/editar_funcionario/get-cidade/<int:idEstado>',views.get_cidade, name='get_cidade'),

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
    path('estoque/fornecedores', listarFornecedores, name = 'fornecedores'),
    path('estoque/fornecedores/novo_fornecedor', criarFornecedor, name = 'novo_fornecedor'),
    path('estoque/fornecedores/editar_fornecedor/<int:idFornecedor>', editarFornecedor, name = 'editar_fornecedor'),
    path('estoque/fornecedores/mostrar_fornecedor/<int:idFornecedor>', showFornecedor, name = 'show_fornecedor'),
    path('estoque/fornecedores/eliminar_fornecedor/<int:idFornecedor>', eliminarFornecedor, name = 'eliminar_fornecedor'),

    #clientes
    path('pessoas/clientes/listclientes', listarClientes, name = 'clientes'),
    path('pessoas/clientes/listclientes/novo_cliente', criarCliente, name = 'novo_cliente'),
    path('pessoas/clientes/listclientes/editar_cliente/<int:idCliente>', editarCliente, name = 'editar_cliente'),
    path('pessoas/clientes/listclientes/mostrar_cliente/<int:idCliente>', showCliente, name = 'show_cliente'),
    path('pessoas/clientes/listclientes/eliminar_cliente/<int:idCliente>', eliminarCliente, name = 'eliminar_cliente'),

    #funcionarios
    path('pessoas/', listarFuncionarios, name = 'funcionarios'),
    path('pessoas/novo_funcionario', criarFuncionario, name = 'novo_funcionario'),
    path('pessoas/editar_funcionario/<int:idFuncionario>', editarFuncionario, name = 'editar_funcionario'),
    path('pessoas/mostrar_funcionario/<int:idFuncionario>', showFuncionario, name = 'show_funcionario'),
    path('pessoas/eliminar_funcionario/<int:idFuncionario>', eliminarFuncionario, name = 'eliminar_funcionario'),

    #tipo de funcionario
    path('pessoas/tipoFuncionario', listarTiposFuncionarios, name = 'tipoFuncionario'),
    path('pessoas/tipoFuncionario/novo_tipoFuncionario', criarTipoFuncionario, name = 'novo_tipoFuncionario'),
    path('pessoas/tipoFuncionario/editar_tipoFuncionario/<int:idTipoFuncionario>', editarTipoFuncionario, name = 'editar_tipoFuncionario'),
    path('pessoas/tipoFuncionario/mostrar_tipoFuncionario/<int:idTipoFuncionario>', showTipoFuncionario, name = 'show_tipoFuncionario'),
    path('pessoas/tipoFuncionario/eliminar_tipoFuncionario/<int:idTipoFuncionario>', eliminarTipoFuncionario, name = 'eliminar_tipoFuncionario'),

    #lanches
    path('lanches/', listarLanches, name = 'lanches'),
    path('lanches/novo_lanche', criarLanche, name = 'novo_lanche'),
    path('lanches/editar_lanche/<int:idLanche>', editarLanche, name = 'editar_lanche'),
    path('lanches/mostrar_lanche/<int:idLanche>', showLanche, name = 'show_lanche'),
    path('lanches/eliminar_lanche/<int:idLanche>', eliminarLanche, name = 'eliminar_lanche'),

    #bebidas
    #path('bebidas/', listarBebidas, name = 'bebidas'),
    #path('bebidas/novo_bebida', criarBebida, name = 'novo_bebida'),
    #path('bebidas/editar_bebida/<int:idBebida>', editarBebida, name = 'editar_bebida'),
    #path('bebidas/mostrar_bebida/<int:idBebida>', showBebida, name = 'show_bebida'),
    #path('bebidas/eliminar_bebida/<int:idBebida>', eliminarBebida, name = 'eliminar_bebida'),
    
]