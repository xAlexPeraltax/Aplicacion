from django.db import models

# Create your models here.
# Clase Autos
class autos (models.Model):
    Marca = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Años = models.CharField(max_length=4)
    Precio = models.IntegerField()
    
