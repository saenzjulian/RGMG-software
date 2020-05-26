from django.db import models

# Create your models here.


class Tabla(models.Model):
    tiempo = models.FloatField(null=True,default= -10)  
    columnaA = models.FloatField(null=True,default= -10)
    columnaB = models.FloatField(null=True,default= -10)
    columnaC = models.FloatField(null=True,default= -10)
    columnaD = models.FloatField(null=True,default= -10)
    columnaE = models.FloatField(null=True,default= -10)
    columnaF = models.FloatField(null=True,default= -10)

class SeleccionTipo(models.Model):
    letraVector = models.CharField(max_length=100)
    tipoVector = models.CharField(max_length=100)


    
   





    
    


