from django.contrib import admin
from .models import SobreInstituicao, Valores, ImagensGaleria, MensagemCoracao, DownloadMateriais
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(SobreInstituicao, SingletonModelAdmin)

admin.site.register(Valores)

admin.site.register(ImagensGaleria)

admin.site.register(MensagemCoracao, SingletonModelAdmin)

admin.site.register(DownloadMateriais, SingletonModelAdmin)