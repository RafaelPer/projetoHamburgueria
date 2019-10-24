from django.db import models
from apps.cidade.models import Cidade
from apps.estado.models import Estado
from apps.pais.models import Pais
from datetime import datetime
# Create your models here.

def user_directory_path(instance, filename):
    _now = datetime.now()
    import os.path
    fn, ext = os.path.splitext(filename)
    return "fornecedores/fornecedor_{id}/{id}_{dia}_{mes}_{ano}_{hora}_{minuto}_{segundos}{ext}".format(id=instance.idFornecedor, dia = _now.strftime('%d'), mes = _now.strftime('%m'), ano = _now.strftime('%Y'), hora = _now.strftime('%H'), minuto = _now.strftime('%M'), segundos = _now.strftime('%S'), ext=ext)

def normalize_ext(image_field):
    try:
        from PIL import Image
    except ImportError:
        import Image
    ext = Image.open(image_field).format
    if hasattr(image_field, 'seek') and callable(image_field.seek):
       image_field.seek(0)
    ext = ext.lower()
    if ext == 'jpeg':
        ext = 'jpg'
    return '.' + ext

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
    foto = models.ImageField(upload_to = user_directory_path, default = 'sem-imagem-avatar.png')
    ativo = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    fornecedorCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    fornecedorEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fornecedorPais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['razao_social']

    def __str__(self):
        return self.razao_social
    
    def save(self, *args, **kwargs):
        if self.idFornecedor is None:
            saved_image = self.foto
            self.foto = None
            super(Fornecedor, self).save(*args, **kwargs)
            self.foto = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Fornecedor, self).save(*args, **kwargs)