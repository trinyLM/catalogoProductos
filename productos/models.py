from typing import Any
from django.db import models

class Categoria(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    marca=models.CharField(max_length=255)
    precio= models.FloatField()
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen=models.ImageField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]




    

    
    

