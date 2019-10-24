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
    return "clientes/cliente_{id}/{id}_{dia}_{mes}_{ano}_{hora}_{minuto}_{segundos}{ext}".format(id=instance.idCliente, dia = _now.strftime('%d'), mes = _now.strftime('%m'), ano = _now.strftime('%Y'), hora = _now.strftime('%H'), minuto = _now.strftime('%M'), segundos = _now.strftime('%S'), ext=ext)

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
    foto = models.ImageField(upload_to = user_directory_path, default = 'sem-imagem-avatar.png')
    ativo = models.CharField(
        max_length = 5,
        choices=STATUS,
    )
    clienteCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    clienteEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    clientePais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.idCliente is None:
            saved_image = self.foto
            self.foto = None
            super(Cliente, self).save(*args, **kwargs)
            self.foto = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Cliente, self).save(*args, **kwargs)