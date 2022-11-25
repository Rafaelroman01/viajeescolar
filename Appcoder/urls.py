from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("participantes/", participantes, name="coder-participantes"),
    path("recreadores/", recreadores, name="coder-recreadores"),
    path("excursiones/", excursiones, name="coder-excursiones"),
    path("excursiones/crear/", creacion_excursion, name="coder-excursiones-crear"),
    path("documentacion/", documentacion, name="coder-documentacion"),
    
]
