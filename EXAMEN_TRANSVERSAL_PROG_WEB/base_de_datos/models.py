from django.db import models
from django.forms import ModelForm
# Create your models here.


class Boleta(models.Model):
    nombre_producto = models.CharField(max_length=30)
    detalle = models.CharField(max_length=30)
    fecha = models.DateField()
    valor= models.IntegerField()
    Total = models.IntegerField()

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    registro = models.BooleanField()
    correoCliente = models.EmailField()

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    disponible = models.BooleanField()
    precio_normal = models.IntegerField(null=True)
    precio_usuario_registrado = models.IntegerField(null=True)

class ProductosAgregados(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio_normal = models.IntegerField(null=True)
    precio_usuario_registrado = models.IntegerField(null=True)

class ProductosAgregados_usuario_registrado(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio_normal = models.IntegerField(null=True)
    precio_usuario_registrado = models.IntegerField(null=True)
    
    

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

class TablaLogin2(models.Model):
    usuario2 = models.CharField(max_length=50)
    contrasena2 = models.CharField(max_length=50)

class registro_usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    