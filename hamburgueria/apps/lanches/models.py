from django.db import models
from apps.tamanhoLanche.models import tamanhoLanche
# Create your models here.

class Lanche(models.Model):
    idLanche = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='')
    preco = models.DecimalField(max_digits=4, decimal_places=2, blank = False, null = False)
    lancheTamanhoLanche = models.ForeignKey(tamanhoLanche, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lanche"
        verbose_name_plural = "Lanches"
        ordering = ['nome']

    def __str__(self):
        return self.nome