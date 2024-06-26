from apps.API_007_InventarioLocal.models import InventarioLocal

def create_inventarioLocal(local, productos, stock):
    return InventarioLocal.objects.create(
        local=local,
        productos=productos,
        stock=stock
    )