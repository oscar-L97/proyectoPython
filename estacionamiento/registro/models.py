from django.db import models
from django.conf import settings

# Create your models here.

class Espacio(models.Model):
    id = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=10)
    id_mat = models.IntegerField(default = 0)
    nom_mat = models.CharField(max_length = 50, blank = True)
    id_int = models.IntegerField(default = 0)
    nom_int = models.CharField(max_length = 50, blank = True)
    id_vesp = models.IntegerField(default = 0)
    nom_vesp = models.CharField(max_length = 50, blank = True)


    def __str__(self):
        return self.identificacion

# class Alumno(models.Model):
#     id = models.IntegerField(default=0)
#     turno = models.IntegerField(default = 0)
#     matricula = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     facultad = models.CharField(max_length=100)
