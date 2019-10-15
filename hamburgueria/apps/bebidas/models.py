from django.db import models
from apps.tamanhoBebidas.models import tamanhoBebida
# Create your models here.

class Bebida(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idBebida = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='texto')
    preco = models.DecimalField(max_digits=4, decimal_places=2, blank = False, null = False)
    isAlcoolico = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    bebidaTamanhoBebida = models.ForeignKey(tamanhoBebida, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"
        ordering = ['nome']

    def __str__(self):
        return self.nome