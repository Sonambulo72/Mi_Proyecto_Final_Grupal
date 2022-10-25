#from unittest.util import _MAX_LENGTH
from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
      return f"{self.nombre},{self.numero_pasaporte}, {self.id}"

# defino nuevas clases
class Auto(models.Model):
    patente = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    kms = models.IntegerField()

    def __str__(self):
      return f"{self.patente},{self.marca},{self.kms}, {self.id}"

class Moto(models.Model):
    patente = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cilindrada = models.IntegerField()
    
    def __str__(self):
      return f"{self.patente}, {self.marca}, {self.cilindrada}, {self.id}"