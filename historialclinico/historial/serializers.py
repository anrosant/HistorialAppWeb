from rest_framework import routers, serializers, viewsets
from historial.models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre_usuario', 'contrasenia')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('cedula', 'nombre', 'apellido', 'correo', 'direccion', 'profesion', 'estado_civil', 'edad',
                  'sexo', 'lugar_nacimiento', 'fecha_nacimiento', 'ocupacion_actual', 'fecha_registro', 'foto', 'nombre_usuario')

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = ('empleado', 'fecha', 'motivo', 'problema_actual', 'revision', 'prescripcion', 'examen_fisico')

class AtencionEnfermeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionEnfermeria
        fields = ('empleado', 'fecha', 'motivo', 'diagnostico', 'plan_cuidados')

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ( 'consulta_medica', 'atencion_enfermeria', 'presion_sistolica', 'presion_distolica', 'pulso','temperatura')
class PermisoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoMedico
        fields = ( 'empleado', 'fecha_inicio', 'fecha_fin', 'dias')
class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ( 'codigo', 'nombre')
class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ( 'permiso_medico', 'consulta_medica', 'enfermedad', 'tipo')
class ChequeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chequeo
        fields = ( 'fecha', 'tipo')
class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = ( 'empleado', 'chequeo', 'foto')
class AntecedentePatologicoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoPersonal
        fields = ( 'ficha_medica', 'consulta_medica', 'lugar_patologia', 'detalle_patologia')
class RevisionAparatoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionAparatoSistema
        fields = ( 'ficha_medica', 'aparato_sistema')
class AparatoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AparatoSistema
        fields = (  'nombre' ,'hallazgo' ,'detalle')
class AntecedenteLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedenteLaboral
        fields = ( 'ficha_medica' ,'edad_inicio' ,'actividad' ,'riesgos' ,'epps' ,'tiempo' , 'cargo')
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('antecedente_laboral', 'nombre', 'factores_riesgo')
class AntecedentePatologicoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoFamiliar
        fields = ('ficha_medica', 'consulta_medica', 'enfermedad', 'parentesco')
class InmunizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmunizacion
        fields = ('ficha_medica', 'observaciones', 'fecha_aplicacion')
class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('inmunizacion', 'nombre', 'numero')
class ExamenLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenLaboratorio
        fields = ('ficha_medica', 'descripcion', 'archivo')
class SomaticoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomaticoGeneral
        fields = ('apariencia', 'estado_nutricional', 'actividades_psicomotoras')
class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = ('piel_tegumentos', 'cabeza_cuello','torax','corazon','pulmones','abdomen')
class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        fields = ('cifosis_acentuada', 'contractura_muscular', 'dolor', 'lordosis_acentuada', 'escoliosis', 'motricidad', 'lassegue', 'detalle')
class RegionLumbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionLumbar
        fields = ('dolor_punio_percusion', 'motricidad', 'detalle')
class ExtremidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extremidades
        fields = ('phalen', 'tinel', 'dolor', 'signo_cajon_rodilla', 'finkelstein', 'motricidad', 'observaciones')
class ExamenFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenFisico
        fields = ('ficha_medica', 'signos_vitales', 'somatico_general', 'regional', 'columna', 'region_lumbar', 'extremidades', 'talla', 'peso', 'indice_masa_corporal')
