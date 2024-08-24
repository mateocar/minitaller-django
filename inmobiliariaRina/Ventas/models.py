from django.db import models
from ..Inmuebles.models import inmueble
from ..Clientes.models import Cliente
from ..Vendedores.models import vendedor
from ..FormasPagos.models import forma_pago

class venta(models.Model):
    id_inmueble = models.ForeignKey(inmueble , on_delete= models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    id_vendedor = models.ForeignKey(vendedor, on_delete= models.CASCADE)
    id_forma_pago = models.ForeignKey(forma_pago, on_delete= models.CASCADE)
    costo_total = models.IntegerField()
