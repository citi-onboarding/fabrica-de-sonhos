from django.db import models
from solo.models import SingletonModel

# Create your models here.

class SobreInstituicao(SingletonModel):
    sobre = models.TextField('Sobre a Instituição', null=True, blank=True)

    class Meta:
        verbose_name = 'Sobre a Instituição'

    def __str__(self):
        return self.name

class Valores(models.Model):
    valor = models.CharField('Valor', max_length=100)
    image = models.ImageField(upload_to='imagemValores/', verbose_name='Imagem do valor', null=True)
    gif = models.ImageField(upload_to='gifValores/', verbose_name='Gif do valor', null=True)

    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'

    def __str__(self):
        return self.name
    