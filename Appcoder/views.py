from django.http import HttpResponse 
from django.shortcuts import render
from Appcoder.models import Excursion

# Create your views here.
def inicio(request):
    return render(request, "Appcoder/inicio.html")

def excursiones(request):
    return HttpResponse("Estas en excursiones")

def participantes(request):
    return HttpResponse("Estas en participantes")

def recreadores(request):
    return HttpResponse("Estas en recreadores")

def documentacion(request):
    return HttpResponse("Estas en documentacion")

# Res   .


