from rest_framework import generics
from apps.API_003_Categorias.models import Categoria
from .serializers import CategoriaSerializer
from .services import delete_categoria, get_categoria, update_categoria

class CategoriaCreateAPIView(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_object(self):
        return get_categoria(self.kwargs['pk'])
    
    def perform_update(self, serializer):
        update_categoria(serializer.instance, **serializer.validated_data)
    
    def perform_destroy(self, instance):
        delete_categoria(instance)

class CategoriaListAPIView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
