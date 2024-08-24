from django.db import models


class tipo_inmueble(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=25, choices=[("CS", "Casa"),("APTO", "Apartamento"),("APTOES", "Aparta Estudio")])

class inmueble(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    id_tipo_inmueble = models.ForeignKey(tipo_inmueble, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length = 25)
    costo = models.BigIntegerField()
    estado = models.CharField(max_length=15, choices=[("DISP", "Diponible"), ("VEND", "Vendido"), ("ARR", "Arrendado")])
