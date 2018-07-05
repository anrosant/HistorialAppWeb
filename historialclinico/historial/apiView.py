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

class CrearSignosVitalesView(generics.ListCreateAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaSignosVitalesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer

class CrearConsultaMedicaView(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaConsultaMedicaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class CrearAtencionEnfermeriaView(generics.ListCreateAPIView):
    queryset = AtencionEnfermeria.objects.all()
    serializer_class = AtencionEnfermeriaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAtencionEnfermeriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AtencionEnfermeria.objects.all()
    serializer_class = AtencionEnfermeriaSerializer