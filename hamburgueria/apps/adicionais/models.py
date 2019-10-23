from django.db import models
from apps.fornecedores.models import Fornecedor
# Create your models here.

class Adicional(models.Model):
    idAdicional = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    quantidade = models.DecimalField(max_digits=10, decimal_places=5, blank = False, null = False)
    unidade = models.CharField(max_length = 3, blank = False, null = False)
    isFalta = models.BooleanField(default=False)
    adicionalFornecedor = models.ManyToManyField(Fornecedor)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Adicional"
        verbose_name_plural = "Adicionais"
        ordering = ['nome']

    def __str__(self):
        return self.nome