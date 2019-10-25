from django.db import models
from apps.pais.models import Pais
# Create your models here.

class Estado(models.Model):
    idEstado = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    uf = models.CharField(max_length = 3, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    estadoPais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['nome']

    def __str__(self):
        return self.nome