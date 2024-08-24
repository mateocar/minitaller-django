from django.db import models

class tipo_inmueble(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=25, choices=[("CS", "Casa"),("APTO", "Apartamento"),("APTOES", "Aparta Estudio")])
