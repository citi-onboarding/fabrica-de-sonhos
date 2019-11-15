from django.shortcuts import render
from django.views import generic
from .models import SobreInstituicao, Valores, ImagensGaleria, MensagemCoracao

class HomeView (generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)

        # Seção 'Sobre nós'
        context["sobreInstituicao"] = SobreInstituicao.objects.all()
        context["valores"] = Valores.objects.all()

        # Seção 'Galeria de Eventos'
        context["imagensGaleria"] = ImagensGaleria.objects.all()
        context["mensagemCoracao"] = MensagemCoracao.objects.all()


        return context
