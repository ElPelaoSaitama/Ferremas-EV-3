from rest_framework import generics, status
from rest_framework.response import Response
from .models import Orden
from .serializers import OrdenSerializer
from .services import crear_orden, actualizar_orden, eliminar_orden, obtener_orden, listar_ordenes

class OrdenCreateAPIView(generics.CreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        detalles = serializer.validated_data.pop('detalles')
        orden = crear_orden(serializer.validated_data['usuario'], detalles)
        output_serializer = OrdenSerializer(orden)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

class OrdenDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def get_object(self):
        orden_id = self.kwargs.get('pk')
        return obtener_orden(orden_id)

    def perform_update(self, serializer):
        estado = serializer.validated_data.get('estado')
        total = serializer.validated_data.get('total', None)
        orden_id = self.kwargs.get('pk')
        actualizar_orden(orden_id, estado, total)

    def perform_destroy(self, instance):
        eliminar_orden(instance.id)

class OrdenListAPIView(generics.ListAPIView):
    serializer_class = OrdenSerializer

    def get_queryset(self):
        usuario = self.request.query_params.get('usuario', None)
        return listar_ordenes(usuario)
