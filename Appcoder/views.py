from django.http import HttpResponse 
from django.shortcuts import render
from Appcoder.models import Excursion



# Create your views here.
def inicio(request):
    return render(request, "Appcoder/index.html")


def excursiones(request):
    return render(request, "Appcoder/excursiones.html")

def participantes(request):
    return render(request, "Appcoder/participantes.html") 

def recreadores(request):
    return render(request, "Appcoder/recreadores.html")

def documentacion(request):
    return render(request, "Appcoder/documentacion.html")

# Res   .


