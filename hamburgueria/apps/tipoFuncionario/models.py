from django.db import models

# Create your models here.

class tipoFuncionario(models.Model):
    idTipoFuncionario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tipoFuncionario"
        verbose_name_plural = "tiposFuncionarios"
        ordering = ['nome']

    def __str__(self):
        return self.nome