from rest_framework import viewsets, generics
from .serializers import MarcaSerializers
from .models import Marca
from .services import get_marca, update_marca, delete_marca

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

class MarcaAPIView(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

class MarcaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

    def get_object(self):
        return get_marca(self.kwargs['pk'])
    
    def perform_update(self, serializer):
        update_marca(serializer.instance, **serializer.validated_data)
    
    def perform_destroy(self, instance):
        delete_marca(instance)