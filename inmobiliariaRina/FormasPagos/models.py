from django.db import models

class forma_pago(models.Model):
    id_forma_pago = models.AutoField(primary_key = True)
    forma_pago = models.CharField(max_length = 25, choices=[("EF", "Efectivo"), ("TRANF", "Transferencia")])
