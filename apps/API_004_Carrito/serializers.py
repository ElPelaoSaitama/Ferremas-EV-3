from rest_framework import serializers
from .models import Carrito, ItemCarrito
from apps.API_001_Productos.serializers import ProductoSerializer

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ItemCarrito
        fields = ['id', 'producto', 'producto_id', 'cantidad', 'subtotal']

    def get_subtotal(self, obj):
        return obj.cantidad * obj.producto.precio

    def create(self, validated_data):
        """Crear o actualizar un ítem en el carrito."""
        producto_id = validated_data.pop('producto_id')
        carrito_id = self.context['carrito_id']
        item, _ = ItemCarrito.objects.update_or_create(
            carrito_id=carrito_id,
            producto_id=producto_id,
            defaults=validated_data
        )
        return item

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'items', 'total']

    def get_total(self, obj):
        """Calcular el total del carrito."""
        return sum(item.get_subtotal() for item in obj.items.all())
