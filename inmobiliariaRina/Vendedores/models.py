from django.db import models

class vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key = True)
    documento = models.IntegerField()
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length = 100)