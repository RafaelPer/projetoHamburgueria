from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    idIngrediente = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    preco = models.DecimalField(max_digits=4, decimal_places=2, blank = False, null = False)
    quantidade = models.DecimalField(max_digits=4, decimal_places=4, blank = False, null = False, default= 0.0000)
    unidade = models.CharField(max_length = 3, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ['nome']

    def __str__(self):
        return self.nome