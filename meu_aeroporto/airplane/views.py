from django.http import HttpResponse
from django.template import loader
from .models import Airplane  

def airplane(request):
    myairplane = Airplane.objects.all() 
    template = loader.get_template('all_airplane.html') 
    context = {
        'myairplane': myairplane, 
    }
    return HttpResponse(template.render(context, request))  

def details(request, id):
    myairplane = Airplane.objects.get(id=id)  
    template = loader.get_template('details.html')  
    context = {
        'myairplane': myairplane,  
    }
    return HttpResponse(template.render(context, request))  

def main(request):
    template = loader.get_template('main.html')  
    return HttpResponse(template.render())  

def testing(request):
    mydata = Airplane.objects.all().order_by('modelo')  
    template = loader.get_template('template.html')  
    context = {
        'myairplane': mydata,  
    }
    return HttpResponse(template.render(context, request))  