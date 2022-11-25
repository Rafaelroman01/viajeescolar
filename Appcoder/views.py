from django.http import HttpResponse 
from django.shortcuts import render
from Appcoder.models import Excursiones
from Appcoder.models import *


# Create your views here.
def inicio(request):
    return render(request, "Appcoder/index.html")


def excursiones(request):
    return render(request, "Appcoder/excursiones.html")

def creacion_excursion(request):
    
    if request.method == "POST":
        destino_excursion = request.POST["lugar"]
        datos_email = request.POST["email"] 
        
        excursion = Excursiones(lugar=destino_excursion, email=datos_email)
        excursion.save()
    
    return render(request, "Appcoder/excursion_formulario.html")

def participantes(request):
    return render(request, "Appcoder/participantes.html") 

def recreadores(request):
    return render(request, "Appcoder/recreadores.html")

def documentacion(request):
    return render(request, "Appcoder/documentacion.html")

# Res   .


