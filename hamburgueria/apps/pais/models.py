from django.db import models

# Create your models here.

class Pais(models.Model):
    idPais = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    sigla = models.CharField(max_length = 5, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['nome']

    def __str__(self):
        return self.nome