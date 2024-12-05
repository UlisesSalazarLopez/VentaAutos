from django.db import models
#Contiene las clases base para definir modelos de bases de datos
# Create your models here.

# Tabla AUTOS
class Autos(models.Model):
    #Defini una clase `Autos`, que representa una tabla en la base de datos
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    #models.CharField = Una cadena de texto
    #models.IntegerField = un número entero