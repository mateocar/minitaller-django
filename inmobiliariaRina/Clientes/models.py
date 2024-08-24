from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key = True)
    documento = models.IntegerField()
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length = 100)


def src(self):
    return f"{self.nombre}"

