from django.db import models
from django.contrib.auth.models import User
from apps.API_001_Productos.models import Producto

class Orden(models.Model):
    # Estado de la orden
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PROCESANDO', 'Procesando'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado')
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordenes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id} - Usuario: {self.usuario.username}"

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.save()

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_por_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle para Orden {self.orden.id} - Producto: {self.producto.nombre}"
