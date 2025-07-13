from django.db import models
from django.core.exceptions import ValidationError

def validar_precio(valor):
    if valor < 0:
        raise ValidationError("El precio no puede ser negativo.")

def validar_stock(valor):
    if valor < 0:
        raise ValidationError("El stock no puede ser negativo.")

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])
    stock = models.IntegerField(validators=[validar_stock])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)

