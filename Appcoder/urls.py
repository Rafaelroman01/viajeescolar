from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("participantes/", participantes),
    path("recreadores/", recreadores),
    path("excursiones/", excursiones),
    path("documentacion/", documentacion)
    
]
