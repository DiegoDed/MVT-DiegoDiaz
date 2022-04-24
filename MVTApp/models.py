from django.db import models

# Create your models here.
class Familia(models.Model):
    
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    edad=models.IntegerField()
    fechaDeNacimiento=models.DateTimeField()