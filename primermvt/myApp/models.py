from django.db import models

# Create your models here.
class DataFamily(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(default= 0)
    fechaNac = models.DateField()


