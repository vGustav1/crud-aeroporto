from django.http import HttpResponse
from django.template import loader
from .models import Airplane  # Certifique-se de importar o modelo correto

def airplane(request):
    myairplane = Airplane.objects.all()  # Obtendo todos os aviões
    template = loader.get_template('all_airplane.html')  # Carregando o template de todos os aviões
    context = {
        'myairplane': myairplane,  # Passando os aviões para o template
    }
    return HttpResponse(template.render(context, request))  # Renderizando a resposta

def details(request, id):
    myairplane = Airplane.objects.get(id=id)  # Obtendo o avião pelo ID
    template = loader.get_template('details.html')  # Carregando o template de detalhes
    context = {
        'myairplane': myairplane,  # Passando o avião para o template
    }
    return HttpResponse(template.render(context, request))  # Renderizando a resposta

def main(request):
    template = loader.get_template('main.html')  # Carregando o template principal
    return HttpResponse(template.render())  # Renderizando a resposta

def testing(request):
    mydata = Airplane.objects.all().order_by('modelo')  # Obtendo todos os aviões ordenados pelo modelo
    template = loader.get_template('template.html')  # Carregando o template de teste
    context = {
        'myairplane': mydata,  # Passando os aviões para o template
    }
    return HttpResponse(template.render(context, request))  # Renderizando a resposta