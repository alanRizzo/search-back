from django.db import models


class Item(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    precio = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}, {}".format(self.codigo, self.nombre)


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.nombre)
