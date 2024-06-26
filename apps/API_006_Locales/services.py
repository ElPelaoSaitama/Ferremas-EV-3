from .models import Local

def crear_local(nombre, direccion, telefono, email, horario_apertura, horario_cierre):
    local = Local.objects.create(
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        email=email,
        horario_apertura=horario_apertura,
        horario_cierre=horario_cierre
    )
    return local

def obtener_local(local_id):
    return Local.objects.get(id=local_id)

def actualizar_local(local, nombre=None, direccion=None, telefono=None, email=None, horario_apertura=None, horario_cierre=None):
    if nombre:
        local.nombre = nombre
    if direccion:
        local.direccion = direccion
    if telefono:
        local.telefono = telefono
    if email:
        local.email = email
    if horario_apertura:
        local.horario_apertura = horario_apertura
    if horario_cierre:
        local.horario_cierre = horario_cierre
    local.save()
    return local

def eliminar_local(local):
    local.delete()
