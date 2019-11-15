from django.shortcuts import render
from django.views import generic
from .models import SobreInstituicao, Valores

class HomeView (generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context["sobreInstituicao"] = SobreInstituicao.objects.all()
        context["valores"] = Valores.objects.all()
        return context
        