from rest_framework import serializers
from .models import *

from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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
        fields = ('pk', 'enfermedad', 'consulta_medica', 'ficha_medica', 'tipoEnfermedad')

class PermisoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoMedico
        fields = ('pk', 'empleado', 'diagnostico', 'consulta_medica', 'fecha_registro', 'doctor', 'fecha_inicio',
                  'fecha_fin', 'dias_permiso', 'observaciones_permiso')

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

class AntecedenteGinecoObstetricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedenteGinecoObstetrico
        fields = ('pk', 'ficha', 'fecha_ultima_menstruacion', 'planificacion_familiar')

class AntecedenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antecedente
        fields = ('pk', 'antecedente_gineco_obstetrico', 'antecedente')

class HabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habito
        fields = ('pk', 'ficha', 'alcohol', 'tabaco', 'cantidad_tabaco')

class AntecedentePatologicoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentePatologicoFamiliar
        fields = ('pk', 'ficha', 'parentesco', 'patologia', 'detalle')

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('pk', 'nombre', 'cargo', 'riesgos', 'epps', 'area_trabajo')

class AntecedenteLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedenteLaboral
        fields = ('pk', 'ficha_medica', 'empresa', 'tiempo', 'edad_inicio', 'actividades_extralaborales', 'actual')

class FactorRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorRiesgo
        fields = ('pk', 'empresa', 'tipo', 'nombre')

class ExamenLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenLaboratorio
        fields = ('pk', 'ficha_medica', 'tipo', 'descripcion', 'imagen')

class ExamenConsultaSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = ExamenConsulta
        fields = ('pk', 'consulta_medica', 'imagen')

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
                  'detalle_alteracion')

class RegionLumbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionLumbar
        fields = ('pk', 'dolor_punio_percusion', 'motricidad', 'detalle_alteracion')

class ExtremidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extremidades
        fields = ('pk', 'dolor', 'motricidad', 'observaciones')

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionLumbar
        fields = ('pk', 'columna', 'extremidades', 'tipo', 'lugar')

class ExamenFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenFisico
        fields = ('pk', 'ficha_medica', 'signos_vitales', 'somatico_general', 'columna', 'region_lumbar', 'extremidades',
                  'regional', 'talla', 'peso', 'indice_masa_corporal', 'examen_neurologico_elemental')

class VulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerabilidad
        fields = ('pk', 'ficha_medica', 'persona_vulnerable', 'persona_discapacidad', 'descripcion')