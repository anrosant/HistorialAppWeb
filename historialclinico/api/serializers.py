from rest_framework import routers, serializers, viewsets
from .models import *

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('pk','cedula', 'nombre', 'apellido', 'correo', 'direccion', 'profesion', 'estado_civil', 'edad',
                  'sexo', 'lugar_nacimiento', 'fecha_nacimiento', 'ocupacion_actual', 'fecha_registro', 'foto')

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = ('pk','empleado', 'fecha', 'motivo', 'problema_actual', 'revision', 'prescripcion', 'examen_fisico')

class AtencionEnfermeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionEnfermeria
        fields = ('pk','empleado', 'fecha', 'motivo', 'diagnostico', 'plan_cuidados')
class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ('pk','consulta_medica', 'atencion_enfermeria', 'empleado', 'presion_sistolica', 'presion_distolica', 'pulso', 'temperatura')
class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ( 'pk','codigo', 'nombre','grupo')
class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('pk', 'consulta_medica', 'enfermedad', 'tipo')
class PermisoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoMedico
        fields = ('pk','diagnostico','empleado', 'consulta_medica', 'fecha_inicio', 'fecha_fin', 'dias', 'observaciones')
class ChequeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chequeo
        fields = ('pk','fecha', 'tipo')
class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = ('pk','empleado', 'chequeo', 'foto')
class AntecedentePatologicoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoPersonal
        fields = ('pk','ficha_medica', 'consulta_medica', 'lugar_patologia', 'detalle_patologia')
class RevisionAparatoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionAparatoSistema
        fields = ('pk','ficha_medica', 'aparato_sistema')
class AparatoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AparatoSistema
        fields = ( 'pk','nombre' ,'hallazgo' ,'detalle')
class AntecedenteLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedenteLaboral
        fields = ('pk','ficha_medica' ,'edad_inicio' ,'actividad' ,'riesgos' ,'epps' ,'tiempo' , 'cargo')
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('pk','antecedente_laboral', 'nombre', 'factores_riesgo')
class AntecedentePatologicoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoFamiliar
        fields = ('pk','ficha_medica', 'consulta_medica', 'enfermedad', 'parentesco')
class InmunizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmunizacion
        fields = ('pk','ficha_medica', 'observaciones', 'fecha_aplicacion')
class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('pk','inmunizacion', 'nombre', 'numero')
class ExamenLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenLaboratorio
        fields = ('pk','ficha_medica', 'descripcion', 'archivo')
class SomaticoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomaticoGeneral
        fields = ('pk','apariencia', 'estado_nutricional', 'actividades_psicomotoras')
class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = ('pk','piel_tegumentos', 'cabeza_cuello','torax','corazon','pulmones','abdomen')
class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        fields = ('pk','cifosis_acentuada', 'contractura_muscular', 'dolor', 'lordosis_acentuada', 'escoliosis', 'motricidad', 'lassegue', 'detalle')
class RegionLumbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionLumbar
        fields = ('pk','dolor_punio_percusion', 'motricidad', 'detalle')
class ExtremidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extremidades
        fields = ('pk','phalen', 'tinel', 'dolor', 'signo_cajon_rodilla', 'finkelstein', 'motricidad', 'observaciones')
class ExamenFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenFisico
        fields = ('pk','ficha_medica', 'signos_vitales', 'somatico_general', 'regional', 'columna', 'region_lumbar', 'extremidades', 'talla', 'peso', 'indice_masa_corporal')
