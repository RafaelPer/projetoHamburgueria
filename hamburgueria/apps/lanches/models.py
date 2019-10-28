from django.db import models
#from apps.tamanhoLanche.models import tamanhoLanche
from apps.ingredientes.models import Ingrediente
from datetime import datetime
# Create your models here.

def user_directory_path(instance, filename):
    _now = datetime.now()
    import os.path
    fn, ext = os.path.splitext(filename)
    return "lanches/lanche_{id}/{id}_{dia}_{mes}_{ano}_{hora}_{minuto}_{segundos}{ext}".format(id=instance.idLanche, dia = _now.strftime('%d'), mes = _now.strftime('%m'), ano = _now.strftime('%Y'), hora = _now.strftime('%H'), minuto = _now.strftime('%M'), segundos = _now.strftime('%S'), ext=ext)

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


class Lanche(models.Model):
    idLanche = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='')
    preco = models.DecimalField(max_digits=4, decimal_places=2, blank = False, null = False)
    #lancheTamanhoLanche = models.ForeignKey(tamanhoLanche, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to = user_directory_path, default = 'sem-imagem-avatar.png')
    lancheIngrediente = models.ManyToManyField(Ingrediente)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lanche"
        verbose_name_plural = "Lanches"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.idLanche is None:
            saved_image = self.foto
            self.foto = None
            super(Lanche, self).save(*args, **kwargs)
            self.foto = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Lanche, self).save(*args, **kwargs)