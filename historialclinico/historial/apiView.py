from rest_framework import generics

from .serializers import *

class CrearUsuarioView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()

class ListaUsuarioView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CrearEmpleadoView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()

class ListaEmpleadoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer