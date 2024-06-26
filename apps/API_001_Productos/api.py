from rest_framework import generics
from apps.API_001_Productos.models import Producto
from apps.API_001_Productos.serializers import ProductoSerializer
from apps.API_001_Productos.services import actualizar_producto, eliminar_producto

class ProductoCreateAPIView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def perform_update(self, serializer):
        actualizar_producto(serializer.instance.id, **serializer.validated_data)

    def perform_destroy(self, instance):
        eliminar_producto(instance.id)

class ProductoListAPIView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
