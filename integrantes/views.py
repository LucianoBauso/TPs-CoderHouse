from django.shortcuts import render
from .models import Integrante, Casa, Auto


# Create your views here.
def home (request):
    integrantes = Integrante.objects.all()
    return render(request, 'integrante.html',{'integrante': integrantes})

def casas (request):
    casas = Casa.objects.all()
    return render(request, 'casas.html',{'casa': casas})

def autos (request):
    autos = Auto.objects.all()
    return render(request, 'autos.html',{'auto': autos})