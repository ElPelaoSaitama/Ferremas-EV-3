from .models import Marca
from django.core.exceptions import ObjectDoesNotExist

def create_marca(nombre):
    return Marca.objects.create(nombre=nombre)

def get_marca(marca_id):
    try:
        return Marca.objects.get(id=marca_id)
    except Marca.DoesNotExist:
        raise ObjectDoesNotExist("La marca con el ID especificado no existe.")

def update_marca(marca_id, nombre=None):
    try:
        marca = Marca.objects.get(id=marca_id)
        if nombre:
            marca.nombre = nombre
        marca.save()
        return marca
    except Marca.DoesNotExist:
        raise ObjectDoesNotExist("La marca con el ID especificado no existe.")

def delete_marca(marca_id):
    try:
        marca = Marca.objects.get(id=marca_id)
        marca.delete()
    except Marca.DoesNotExist:
        raise ObjectDoesNotExist("La marca con el ID especificado no existe.")
