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
                  'sexo', 'lugar_nacimiento', 'fecha_nacimiento', 'ocupacion_act', 'fecha_registro', 'foto', 'usuario')

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ('presion_sistolica', 'presion_distolica', 'pulso', 'temperatura', 'consulta_medica')

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = ('empleado', 'fechaConsulta', 'probActual', 'motivo', 'revision_medica', 'examen_fisico')

class AtencionEnfermeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionEnfermeria
        fields = ('fechaAtencion', 'empleado', 'motivoAtencion', 'diagnosticoEnfermeria', 'planCuidados')