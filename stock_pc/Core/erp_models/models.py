from django.db import models
from django.utils import timezone


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=30,  verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        db_table = 'empleado_tipos'
        verbose_name_plural = 'Tipos'

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')

class Employee(models.Model):
     categ = models.ManyToManyField(Category)
     type = models.ForeignKey(Type, on_delete=models.CASCADE)
     names = models.CharField(max_length=20, verbose_name='Nombres')
     dni = models.IntegerField(unique=True, verbose_name='DNI')
     date_joined = models.DateField(default=timezone.now, verbose_name='Fecha de Registro')

     def __str__(self):
         return self.names

     class Meta:
         verbose_name = 'Empleado'
         verbose_name_plural = 'Empleados'
         db_table = 'empleado'
         ordering = ['id']
