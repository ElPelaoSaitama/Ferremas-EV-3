from rest_framework import serializers
from django.contrib.auth.models import User
from apps.API_001_Productos.models import Producto
from .models import Orden, DetalleOrden

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Ajusta los campos según lo que necesites exponer

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DetalleOrden
        fields = ['id', 'orden', 'producto', 'producto_id', 'precio_por_unidad', 'cantidad']

class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True, read_only=True)
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Orden
        fields = ['id', 'usuario', 'usuario_id', 'fecha_creacion', 'fecha_actualizacion', 'estado', 'total', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        orden = Orden.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetalleOrden.objects.create(orden=orden, **detalle_data)
        return orden

    def update(self, instance, validated_data):
        instance.estado = validated_data.get('estado', instance.estado)
        instance.total = validated_data.get('total', instance.total)
        instance.save()
        return instance
