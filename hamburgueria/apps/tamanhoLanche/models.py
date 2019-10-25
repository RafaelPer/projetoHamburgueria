from django.db import models
# Create your models here.

class tamanhoLanche(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idTamanhoLanche = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='')
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tamanhoLanche"
        verbose_name_plural = "tamanhosLanches"
        ordering = ['nome']

    def __str__(self):
        return self.nome