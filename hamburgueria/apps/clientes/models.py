from django.db import models
from apps.cidade.models import Cidade
# Create your models here.

class Cliente(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idCliente = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    sobrenome = models.CharField(max_length = 100, blank = False, null = False)
    rg = models.CharField(max_length = 10, blank = False, null = False)
    cpf = models.CharField(max_length = 12, blank = False, null = False)
    rua = models.CharField(max_length = 100, blank = False, null = False)
    bairro = models.CharField(max_length = 100, blank = False, null = False)
    cep = models.CharField(max_length = 9, blank = False, null = False)
    email = models.EmailField(max_length = 100, blank = False, null = False)
    numeroCasa = models.CharField(max_length = 6, blank = False, null = False)
    telefone1 = models.CharField(max_length = 24, blank = False, null = False)
    telefone2 = models.CharField(max_length = 24, blank = False, null = False)
    celular1 = models.CharField(max_length = 24, blank = False, null = False)
    celular2 = models.CharField(max_length = 24, blank = False, null = False)
    foto = models.ImageField(upload_to = 'clientes/%d%m%Y', default = 'sem-imagem-avatar.png')
    ativo = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    clienteCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']

    def __str__(self):
        return self.nome