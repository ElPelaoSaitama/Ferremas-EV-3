from django.db import models
from apps.API_001_Productos.models import Producto
from apps.API_006_Locales.models import Local

class InventarioLocal(models.Model):
    local = models.ForeignKey(Local, on_delete=models.PROTECT)
    productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.local.nombre} - {self.productos.nombre}'