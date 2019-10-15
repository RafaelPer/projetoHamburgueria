from django.db import models
from apps.cidade.models import Cidade
from apps.tipoFuncionario.models import tipoFuncionario
from datetime import datetime
# Create your models here.
class Funcionario(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idFuncionario = models.AutoField(primary_key = True)
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
    foto = models.ImageField(upload_to = 'funcionarios/%d%m%Y', default = 'sem-imagem-avatar.png')
    ativo = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    funcionarioCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    funcionarioTipoFuncionario = models.ForeignKey(tipoFuncionario, on_delete=models.CASCADE)
    senha = models.CharField(max_length=50, blank = False, null = False, default='')
    data_admissao = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ['nome']

    def __str__(self):
        return self.nome