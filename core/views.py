from django.shortcuts import render
from django.views import generic
from .models import SobreInstituicao, Valores, ImagensGaleria, MensagemCoracao, DownloadMateriais
from django.http import HttpResponse
from django.core.mail import EmailMessage

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

        # Seção 'Download de Materiais'
        context["downloadMateriais"] = DownloadMateriais.objects.all()
        return context


def index(request):
    return render(request, 'home.html')


def email(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    telefone = request.POST.get('telephone')
    assunto = request.POST.get('subject')
    mensagem = request.POST.get('message')


    subject = assunto
    body = f'Nome: {nome}\nAssunto: {assunto}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}'

    mail  = EmailMessage(subject, body, 'desafioPTAdjangoCITi2019.2@gmail.com', ['desafioPTAdjangoCITi2019.2@gmail.com', 'rmr@cin.ufpe.br'])
    result = mail.send()
    return HttpResponse(status=201)