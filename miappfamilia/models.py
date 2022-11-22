from django.db import models

# Create your models here.
class Datos_familia(models.Model):
    Nombre = models.CharField(max_length=30)
    Edad = models.IntegerField(default=0)
    F_Nacimiento = models.DateField()
    Sexo = models.CharField(max_length=30)

class  pantalones(models.Model): 
    Nombre = models.CharField(max_length=30)
    Talle = models.IntegerField(default=0)
    color = models.CharField(max_length=30)
    
class camisas(models.Model):
    Nombre = models.CharField(max_length=30)    
    Talle = models.IntegerField(default=0)
    color = models.CharField(max_length=30)