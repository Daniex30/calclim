from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=25
    )
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE
    )
    nombre = models.CharField(
        max_length=30
    )
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    estado = models.BooleanField(
        'activo', default=True
    )
    def __str__(self):
        return str(self.categoria) + ' ' + self.nombre + ' ' + str(self.precio) + ' ' + str(self.cantidad) 