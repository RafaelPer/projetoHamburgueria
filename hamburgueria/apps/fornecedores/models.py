from django.db import models
from apps.cidade.models import Cidade
# Create your models here.

class Fornecedor(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idFornecedor = models.AutoField(primary_key = True)
    razao_social = models.CharField(max_length = 100, blank = False, null = False)
    cnpj = models.CharField(max_length = 15, blank = False, null = False)
    ie = models.CharField(max_length = 12, blank = False, null = False)
    rua = models.CharField(max_length = 100, blank = False, null = False)
    bairro = models.CharField(max_length = 100, blank = False, null = False)
    cep = models.CharField(max_length = 9, blank = False, null = False)
    email = models.EmailField(max_length = 100, blank = False, null = False)
    numeroLocal = models.CharField(max_length = 6, blank = False, null = False)
    telefone1 = models.CharField(max_length = 24, blank = False, null = False)
    telefone2 = models.CharField(max_length = 24, blank = False, null = False)
    celular1 = models.CharField(max_length = 24, blank = False, null = False)
    celular2 = models.CharField(max_length = 24, blank = False, null = False)
    foto = models.ImageField(upload_to = 'funcionarios/%d%m%Y', default = 'sem-imagem-avatar.png')
    ativo = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    fornecedorCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['razao_social']

    def __str__(self):
        return self.razao_social