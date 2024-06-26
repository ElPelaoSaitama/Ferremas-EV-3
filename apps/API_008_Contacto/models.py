from django.db import models

# Create your models here.

class Asunto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    asunto = models.ForeignKey(Asunto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
