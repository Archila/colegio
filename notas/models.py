from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Alumno (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    carnet = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Profesor (models.Model):
    nombre =   models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    salario = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Grado(models.Model):
    nombre    = models.CharField(max_length=30)
    seccion = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre+" - "+self.seccion

class Curso (models.Model):
    nombre    = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Nota (models.Model):
    total    = models.CharField(max_length=5)
    zona    = models.CharField(max_length=4)
    final    = models.CharField(max_length=4)
    curso = models.ForeignKey(Curso)
    alumno = models.ForeignKey(Alumno)
    encargado = models.ForeignKey(Profesor)

    def __str__(self):
        return self.total


class Pensum (models.Model):

    fecha = models.DateTimeField(default=timezone.now)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
