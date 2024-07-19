from .models import Orden, DetalleOrden
from django.db import transaction

def crear_orden(usuario, detalles):
    """
    Crea una orden y sus detalles asociados.
    """
    with transaction.atomic():
        orden = Orden(usuario=usuario)
        orden.save()
        total = 0
        for detalle in detalles:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            precio = producto.precio
            total += precio * cantidad
            DetalleOrden.objects.create(
                orden=orden,
                producto=producto,
                cantidad=cantidad,
                precio_por_unidad=precio
            )
        orden.total = total
        orden.save()
        return orden

def actualizar_orden(orden_id, estado, total=None):
    """
    Actualiza la información de una orden existente.
    """
    orden = Orden.objects.get(id=orden_id)
    orden.estado = estado
    if total is not None:
        orden.total = total
    orden.save()
    return orden

def eliminar_orden(orden_id):
    """
    Elimina una orden y sus detalles asociados.
    """
    with transaction.atomic():
        orden = Orden.objects.get(id=orden_id)
        orden.detalleorden_set.all().delete()  # Elimina todos los detalles asociados
        orden.delete()

def obtener_orden(orden_id):
    """
    Obtiene una orden por su ID.
    """
    return Orden.objects.get(id=orden_id)

def listar_ordenes(usuario=None):
    """
    Lista todas las órdenes, opcionalmente filtradas por usuario.
    """
    if usuario:
        return Orden.objects.filter(usuario=usuario)
    return Orden.objects.all()
