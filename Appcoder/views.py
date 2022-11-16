from django.shortcuts import render

# Create your views here.
from Appcoder.models import viajes

def mostrar_familiares(request):
    f1 = viajes(nombre="Carlos Roman", edad=44, nacimiento="1978-11-13")
    f2 = viajes(nombre="Martin Roman", edad=23, nacimiento="1999-01-07")
    f3 = viajes(nombre="Maria Roman", edad=22, nacimiento="2000-08-25")
    return render(request, "familia.html", {"familia":[f1, f2, f3]})