from apps.API_003_Categorias.models import Categoria

def create_categoria(nombre):
    return Categoria.objects.create(nombre=nombre)

def get_categoria(categoria_id):
    return Categoria.objects.get(id=categoria_id)

def update_categoria(categoria, nombre=None):
    if nombre:
        categoria.nombre = nombre
    categoria.save()
    return categoria

def delete_categoria(categoria):
    categoria.delete()
