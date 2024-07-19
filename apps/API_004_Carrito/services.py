from .models import Carrito, ItemCarrito
from apps.API_001_Productos.models import Producto
from django.core.exceptions import ObjectDoesNotExist

def crear_carrito(usuario):
    """ Crea un nuevo carrito para el usuario. """
    carrito = Carrito.objects.create(usuario=usuario)
    return carrito

def agregar_producto_a_carrito(carrito_id, producto_id, cantidad):
    """ Agrega un producto al carrito o actualiza la cantidad si el producto ya está en el carrito. """
    try:
        carrito = Carrito.objects.get(id=carrito_id)
        producto = Producto.objects.get(id=producto_id)
        item, creado = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': cantidad}
        )
        if not creado:
            item.cantidad += cantidad
            item.save()
        return item
    except ObjectDoesNotExist as e:
        raise ValueError(f"Error al agregar producto al carrito: {str(e)}")

def obtener_carrito(carrito_id):
    """ Retorna un carrito y sus ítems. """
    try:
        carrito = Carrito.objects.get(id=carrito_id)
        carrito.items = carrito.itemcarrito_set.all()
        return carrito
    except Carrito.DoesNotExist:
        raise ValueError("Carrito no encontrado")

def actualizar_cantidad_item(item_id, nueva_cantidad):
    """ Actualiza la cantidad de un ítem específico en el carrito. """
    try:
        item = ItemCarrito.objects.get(id=item_id)
        if nueva_cantidad > 0:
            item.cantidad = nueva_cantidad
            item.save()
        else:
            item.delete()  # Elimina el ítem si la cantidad es cero
        return item
    except ItemCarrito.DoesNotExist:
        raise ValueError("Ítem no encontrado en el carrito")

def eliminar_item_del_carrito(item_id):
    """ Elimina un ítem del carrito. """
    try:
        item = ItemCarrito.objects.get(id=item_id)
        item.delete()
    except ItemCarrito.DoesNotExist:
        raise ValueError("Ítem no encontrado en el carrito")

def vaciar_carrito(carrito_id):
    """ Elimina todos los ítems de un carrito. """
    try:
        carrito = Carrito.objects.get(id=carrito_id)
        carrito.itemcarrito_set.all().delete()
    except Carrito.DoesNotExist:
        raise ValueError("Carrito no encontrado")
