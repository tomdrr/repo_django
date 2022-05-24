from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)  #model como va a ser el dataset en la base de datos sql
    camada = models.IntegerField()       #ya creada la app, voy a settings y "registro" la nueva app
    fecha = models.Field() #agrega una fecha