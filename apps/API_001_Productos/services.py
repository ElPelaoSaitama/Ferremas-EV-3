from .models import Producto

def crear_producto(nombre, precio, descripcion, nuevo, marca, categoria, imagen=None):
    producto = Producto(
        nombre=nombre,
        precio=precio,
        descripcion=descripcion,
        nuevo=nuevo,
        marca=marca,
        categoria=categoria,
        imagen=imagen
    )
    producto.save()
    return producto

def actualizar_producto(producto_id, nombre, precio, descripcion, nuevo, marca, categoria, imagen=None):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        raise ValueError("Producto no encontrado")

    producto.nombre = nombre
    producto.precio = precio
    producto.descripcion = descripcion
    producto.nuevo = nuevo
    producto.marca = marca
    producto.categoria = categoria
    if imagen:
        producto.imagen = imagen
    producto.save()
    return producto

def eliminar_producto(producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        raise ValueError("Producto no encontrado")

    producto.delete()
