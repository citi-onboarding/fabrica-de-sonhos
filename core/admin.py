from django.contrib import admin
from .models import SobreInstituicao, Valores
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(SobreInstituicao, SingletonModelAdmin)
admin.site.register(Valores)