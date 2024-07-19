from rest_framework import generics, status
from rest_framework.response import Response
from .models import Carrito, ItemCarrito
from .serializers import CarritoSerializer, ItemCarritoSerializer
from .services import (
    crear_carrito, agregar_producto_a_carrito, obtener_carrito,
    actualizar_cantidad_item, eliminar_item_del_carrito, vaciar_carrito
)

class CarritoCreateAPIView(generics.CreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def perform_create(self, serializer):
        # Suponiendo que 'usuario' se pasa como parte del request, ajusta según tu modelo de autenticación
        usuario = self.request.user
        serializer.save(usuario=usuario)

class CarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def get_object(self):
        carrito_id = self.kwargs.get('pk')
        return obtener_carrito(carrito_id)

    def perform_update(self, serializer):
        carrito_id = self.kwargs.get('pk')
        data = serializer.validated_data
        producto_id = data.get('producto_id')
        cantidad = data.get('cantidad')
        agregar_producto_a_carrito(carrito_id, producto_id, cantidad)
        serializer.save()

    def perform_destroy(self, instance):
        carrito_id = instance.id
        vaciar_carrito(carrito_id)

class ItemCarritoUpdateAPIView(generics.UpdateAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

    def perform_update(self, serializer):
        item_id = self.kwargs.get('pk')
        nueva_cantidad = serializer.validated_data.get('cantidad')
        actualizar_cantidad_item(item_id, nueva_cantidad)
        serializer.save()

class ItemCarritoDeleteAPIView(generics.DestroyAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

    def perform_destroy(self, instance):
        item_id = instance.id
        eliminar_item_del_carrito(item_id)

# Asegúrate de que los nombres de las clases y métodos coincidan con tus necesidades y modelo de datos.
