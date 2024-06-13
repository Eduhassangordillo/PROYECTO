from django.db import models

class Bici(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    anio = models.IntegerField(default=2010)
    
    def __str__(self):
        return f'Soy la bici {self.modelo} {self.marca}'