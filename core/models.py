from django.db import models
from solo.models import SingletonModel

# Create your models here.


# Seção 'Sobre nós'
class SobreInstituicao(SingletonModel):
    sobre = models.TextField('Sobre a Instituição', null=True, blank=True)

    class Meta:
        verbose_name = 'Sobre a Instituição'

    def __str__(self):
        return self.sobre

class Valores(models.Model):
    valor = models.CharField('Valor', max_length=100)
    image = models.ImageField(upload_to='imagemValores/', verbose_name='Imagem do valor', null=True)
    gif = models.ImageField(upload_to='gifValores/', verbose_name='Gif do valor', null=True)

    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'

    def __str__(self):
        return self.valor


# Seção 'Galeria de eventos'
class ImagensGaleria(models.Model):
    image = models.ImageField(upload_to='imagensGaleria/', verbose_name='Imagem do evento', null=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = "Imagens dos eventos"

class MensagemCoracao(SingletonModel):
    message = models.CharField('Mensagem_coracao', max_length=200)

    class Meta:
        verbose_name = 'Mensagem do coração'


    def __str__(self):
        return self.message

# Seção 'Download de materiais"
class DownloadMateriais(SingletonModel):
    arquivoParaDownload = models.FileField(upload_to='arquivoDownload/', verbose_name='Material para download')
    linkParaTeste = models.URLField('Link para teste', max_length=254, null=True)

    class Meta:
        verbose_name = 'Material da semana'