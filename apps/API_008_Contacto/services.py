from apps.API_008_Contacto.models import Contacto, Asunto
from django.core.exceptions import ObjectDoesNotExist

# Services para flujo de creacion de asunto
def create_asunto(nombre):
    return Asunto.objects.create(nombre=nombre)

def get_asunto(asunto_id):
    try:
        return Asunto.objects.get(id=asunto_id)
    except Asunto.DoesNotExist:
        raise ObjectDoesNotExist("El asunto con el ID especificado no existe.")

def update_asunto(asunto, nombre=None):
    if nombre:
        asunto.nombre = nombre
    asunto.save()
    return Asunto

def delete_asunto(asunto):
    asunto.delete()

# Services para flujo creacion de contacto

def create_contacto(nombre, email, telefono, mensaje, asunto):
    return Contacto.objects.create(
        nombre=nombre,
        email=email,
        telefono=telefono,
        mensaje=mensaje,
        asunto=asunto
    )

def get_contacto(contacto_id):
    return Contacto.objects.get(id=contacto_id)


def update_contacto(contacto_id,nombre, email, telefono, mensaje, asunto):
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.nombre = nombre
    contacto.email = email
    contacto.telefono = telefono
    contacto.mensaje = mensaje
    contacto.asunto = asunto
    contacto.save()
    return contacto

def delete_contacto(contacto):
    contacto.delete()



    """
    def get_contacto(contacto_id):
    try:
        return Contacto.objects.get(id=contacto_id)
    except Contacto.DoesNotExist:
        raise ObjectDoesNotExist("El contacto con el ID especificado no existe.")
    """