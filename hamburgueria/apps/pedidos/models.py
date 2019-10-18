from django.db import models
from apps.lanches.models import Lanche
from apps.bebidas.models import Bebida
from apps.funcionarios.models import Funcionario
from apps.clientes.models import Cliente
from apps.adicionais.models import Adicional
from datetime import datetime
# Create your models here.

class Pedido(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idPedido = models.AutoField(primary_key = True)
    dataPedido = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
    dataFinalPedido = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
    isDelivery = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    mesa = models.CharField(max_length = 5, blank = False, null = False)
    estadoPedido = models.CharField(max_length = 50, blank = False, null = False)
    totalpedido = models.DecimalField(max_digits=4, decimal_places=2, blank = False, null = False)
    isKitchenRequest = models.BooleanField(default=False)
    isBarRequest = models.BooleanField(default=False)
    kitchenFinishing = models.BooleanField(default=False)
    bartenderFinishing = models.BooleanField(default=False)
    pedidoFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    pedidoCliente = models.ManyToManyField(Cliente)
    pedidoBebida = models.ManyToManyField(Bebida)
    pedidoLanche = models.ManyToManyField(Lanche)
    pedidoAdicional = models.ManyToManyField(Adicional)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['dataPedido']

    def __str__(self):
        return self.dataPedido