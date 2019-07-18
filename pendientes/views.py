from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import Tarea #Importamos la clase tarea de models

# Create your views here.

def index(request):
    listita = Tarea.objects.all() #Consultamos la BD y exportamos los registros como objetos de la clase tarea
    persona = {
        "nombre":"Kim",
        "edad": 24,
        "hobbies": ["Ver pelis","Dibujar","Nadar"],
        "Tareas": listita, #Completamos el diccionario con la lista en la clave Tareas para enviar a template
        } 
    return render(request, 'inicio.html', persona) #retornamos el saludo

def pestañas(request):
    saludo = "Hola, Mundo! Esta es la pestaña /"
    return HttpResponse(saludo)

def info(request):
    informacion = "<h1>Penguin Bootcamp</h1><br><p>Esta página fue creada en el Penguin Bootcamp 4. Paraguay, 2019.</p>"
    return HttpResponse(informacion)

def aleatorio(request):
    numero = str(randint(500,999))
    return HttpResponse('El numero ganador es: ' + numero)