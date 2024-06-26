from rest_framework import generics
from apps.API_007_InventarioLocal.models import InventarioLocal
from apps.API_007_InventarioLocal.serializers import InventarioLocalSerializer
from apps.API_007_InventarioLocal.services import create_inventarioLocal

class InventarioLocalCreateAPIVew(generics.CreateAPIView):
    queryset = InventarioLocal.objects.all()
    serializer_class = InventarioLocalSerializer

class InventarioLocalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventarioLocal.objects.all()
    serializer_class = InventarioLocalSerializer

    def get_object(self):
        return create_inventarioLocal(self.kwargs['pk'])