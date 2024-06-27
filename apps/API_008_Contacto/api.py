from rest_framework import generics
from apps.API_008_Contacto.models import Asunto, Contacto
from apps.API_008_Contacto.serializers import AsuntoSerializers, ContactoSerializers
from apps.API_008_Contacto.services import get_asunto,update_asunto,delete_asunto
from apps.API_008_Contacto.services import get_contacto, update_contacto, delete_contacto
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status


# Flujo CRUD Asunto
class AsuntoCreateAPIView(generics.CreateAPIView):
    queryset = Asunto.objects.all()
    serializer_class = AsuntoSerializers

class AsuntoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asunto.objects.all()
    serializer_class = AsuntoSerializers

    def get(self, request, pk, format=None):
        try:
            marca = get_asunto(pk)
            serializer = AsuntoSerializers(marca)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"detalle": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def perform_update(self, serializer):
        update_asunto(serializer.instance, **serializer.validated_data)

    def perform_destroy(self, instance):
        delete_asunto(instance)

class AsuntoListAPIView(generics.ListAPIView):
    queryset = Asunto.objects.all()
    serializer_class = AsuntoSerializers

# Flujo CRUD Contacto

class ContactoCreateAPIView(generics.CreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializers

class ContactoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializers

    def get(self, request, pk , format=None):
        try:
            contacto = get_contacto(pk)
            serializer = ContactoSerializers(contacto)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        update_contacto(serializer.instance, **serializer.validated_data)

    def perform_destroy(self, instance):
        delete_contacto(instance)
    
class ContactoListAPIView(generics.ListAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializers
