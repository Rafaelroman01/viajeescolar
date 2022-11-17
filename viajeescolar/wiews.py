from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from appcododer.views import Excursion

def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba</p>
    """)
def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y tu password por whatsapp")



def dia_hoy(request):
    hoy = datetime.now()
    
    
    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)
def anio_nacimiento(request,edad):
    edad = int(edad)
     
    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}") 





def vista_plantilla(request):
    archivo = open("C:/Users/Familia/Documents/Coder05112022/nuevocoder51122/nuevocoder51122/templates/plantilla_bonita.html")
    plantilla = Template(archivo.read())
    
    archivo.close()
    
    datos = datos = {"nombre": "Leonel", "fecha": datetime.now(), "apellido": "Gareis"}
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo = open("C:/Users/Familia/Documents/Coder05112022/nuevocoder51122/nuevocoder51122/templates/listado_alumnos.html")
    
    plantilla = Template(archivo.read())
    
    archivo.close()
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    plantilla= loader.get_template(vista_listado_alumnos.html)
    documento = plantilla.render(datos)
    return HttpResponse(documento)