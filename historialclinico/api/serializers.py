from rest_framework import serializers
from .models import *

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('pk', 'foto', 'cedula', 'nombre', 'apellido', 'edad', 'sexo', 'estadoCivil', 'lugarNacimiento', 'fechaNacimiento',
                  'direccion', 'correo', 'instruccion', 'profesion', 'ocupacion', 'fechaRegistro', 'ficha_actual')

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = ('pk','empleado', 'examen_fisico', 'fechaConsulta', 'prescripcion', 'motivo', 'prob_actual', 'revision_medica')

class AtencionEnfermeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionEnfermeria
        fields = ('pk','empleado', 'motivoAtencion', 'planCuidados', 'fechaAtencion', 'diagnosticoEnfermeria')

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ('pk', 'empleado', 'consulta_medica', 'atencion_enfermeria', 'fecha', 'presion_sistolica', 'presion_distolica',
                  'pulso', 'temperatura')

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ( 'pk','codigo', 'nombre', 'grupo')

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('pk', 'enfermedad', 'consulta_medica', 'tipoEnfermedad')

class PermisoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoMedico
        fields = ('pk', 'empleado', 'diagnostico', 'consulta_medica', 'doctor', 'fecha_inicio', 'fecha_fin', 'dias_permiso',
                  'observaciones_permiso')

class InmunizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmunizacion
        fields = ('pk', 'observacion')

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('pk','inmunizacion', 'nombre', 'dosis', 'fecha')

class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = ('pk', 'empleado', 'inmunizacion', 'fecha', 'ciudad', 'tipo')

class AparatoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AparatoSistema
        fields = ( 'pk', 'ficha_medica', 'nombre', 'detalle')

class AntecedentePatologicoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoPersonal
        fields = ('pk', 'ficha', 'consulta_medica', 'lugar', 'detalle')

class AntecedentePatologicoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoFamiliar
        fields = ('pk', 'ficha', 'parentesco', 'patologia', 'detalle')

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('pk', 'nombre', 'cargo', 'actividad', 'epps')

class AntecedenteLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedenteLaboral
        fields = ('pk', 'ficha_medica', 'empresa', 'tiempo', 'edad_inicio', 'actual')

class FactorRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorRiesgo
        fields = ('pk', 'empresa', 'tipo', 'nombre')

class ExamenLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenLaboratorio
        fields = ('pk', 'ficha_medica', 'consulta_medica', 'nombre', 'descripcion', 'imagen')

class SomaticoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomaticoGeneral
        fields = ('pk', 'apariencia', 'estado_nutricional', 'actividades_psicomotoras')

class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = ('pk', 'piel_tegumentos', 'cabeza_cuello', 'torax', 'corazon', 'pulmones', 'abdomen')

class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        fields = ('pk', 'cifosis_acentuada', 'contractura_muscular', 'dolor', 'lordosis_acentuada', 'escoliosis', 'motricidad',
                  'lassegue', 'detalle_alteracion')

class LumbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lumbar
        fields = ('pk', 'dolor_punio_percusion', 'motricidad', 'detalle_alteracion')

class ExtremidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extremidades
        fields = ('pk', 'dolor', 'phalen', 'tinel', 'signo_cajon_rodilla', 'finkelstein', 'motricidad', 'observaciones')

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lumbar
        fields = ('pk', 'columna', 'extremidades', 'lugar')

class ExamenFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenFisico
        fields = ('pk', 'ficha_medica', 'signos_vitales', 'somatico_general', 'columna', 'lumbar', 'extremidades',
                  'regional', 'talla', 'peso', 'indice_masa_corporal')