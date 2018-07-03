from rest_framework import routers, serializers, viewsets
from historial.models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('usuario', 'contrasenia')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('cedula', 'nombre', 'apellido', 'correo', 'direccion', 'profesion', 'estado_civil', 'edad',
                  'sexo', 'lugar_nacimiento', 'fecha_nacimiento', 'ocupacion_act', 'fecha_registro', 'foto')