from django.db import models

# Create your models here.


class Cantante(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    genero = models.CharField(max_length=40)

    def __str__(self):

        return f"CANTANTE: {self.nombre} EDAD: {self.edad} GENERO: {self.genero}"


class Cancion(models.Model):

    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField()
    genero = models.CharField(max_length=40)

    def __str__(self):

        return f"CANCION: {self.nombre} DURACION: {self.duracion} GENERO: {self.genero}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):

        return f"USUARIO: {self.nombre} MAIL: {self.mail} EDAD: {self.edad}"
