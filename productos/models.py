from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=True)

    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.precio
    