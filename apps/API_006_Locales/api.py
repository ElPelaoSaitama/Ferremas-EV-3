from rest_framework import generics
from .models import Local
from .serializers import LocalSerializer, LocalCreateSerializer
from .services import eliminar_local, obtener_local, actualizar_local

class LocalCreateAPIView(generics.CreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalCreateSerializer

class LocalListAPIView(generics.ListAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

    def get_object(self):
        return obtener_local(self.kwargs['pk'])

    def perform_update(self, serializer):
        actualizar_local(serializer.instance, **serializer.validated_data)

    def perform_destroy(self, instance):
        eliminar_local(instance)
