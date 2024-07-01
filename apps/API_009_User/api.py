from rest_framework import generics
from django.contrib.auth.models import User


from .serializers import UserRegistrationSerializer, UserUpdateSerializer, UserSerializer
from .services import delete_user, get_user, update_user, dell_user
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_object(self):
        return get_user(self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return self.serializer_class
    
    def perform_update(self, serializer):
        update_user(serializer.instance, **serializer.validated_data)
    
    def perform_destroy(self, instance):
        delete_user(instance)
    
    def delete(self, request, pk, format=None):
        try:
            user = dell_user(pk)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            user = update_user(pk, **request.data)
            if isinstance(user, str):
                return Response({"message": user}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        try:
            user = update_user(pk, **request.data)
            if isinstance(user, str):
                return Response({"message": user}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"Detalle": str(e)}, status=status.HTTP_400_BAD_REQUEST)  
        

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer