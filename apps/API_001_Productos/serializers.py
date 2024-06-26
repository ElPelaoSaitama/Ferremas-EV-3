from rest_framework import serializers
from apps.API_001_Productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio', 'descripcion', 'nuevo', 'marca', 'categoria', 'imagen')