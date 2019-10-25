from django.db import models
from apps.estado.models import Estado
# Create your models here.

class Cidade(models.Model):
    idCidade = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cidadeEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nome']

    def __str__(self):
        return self.nome