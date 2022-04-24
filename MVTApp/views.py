from django.http import HttpResponse
from django.shortcuts import render
from MVTApp.models import Familia
from django.template import loader

# Create your views here.

def familiares(self):
    
    miembro1= Familia(nombre='Gabriel', apellido= 'Diaz', edad=51, fechaDeNacimiento='1971-04-03')
    
    miembro1.save()
    
    miembro2= Familia(nombre='Vero', apellido= 'Comis', edad=52, fechaDeNacimiento='1970-09-29')
    
    miembro2.save()
    
    plantilla = loader.get_template('plantilla1.html')
    
    diccionario= {'nombre1':miembro1.nombre, 'apellido1': miembro1.apellido, 'edad1':miembro1.edad, 'fechaDeNacimiento1':miembro1.fechaDeNacimiento,
                  'nombre2':miembro2.nombre, 'apellido2': miembro2.apellido, 'edad2':miembro2.edad, 'fechaDeNacimiento2':miembro2.fechaDeNacimiento
                  }
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
    