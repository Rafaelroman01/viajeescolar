from django.urls import path
from Appcoder.views import mostrar_familiares

urlpatterns = [
    path("viajes/", mostrar_familiares)
    
]
