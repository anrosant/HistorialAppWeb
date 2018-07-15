from django.db import models
from django.utils import timezone

DEFAULT = 0
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=16)
    contrasenia = models.CharField(max_length=16)

    def __str__(self):
        return "{}".format(self.nombre_usuario)

class Empleado(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=10)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=9)
    lugar_nacimiento = models.CharField(max_length=20)
    lugar_nacimiento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(default=timezone.now())
    ocupacion_actual = models.CharField(max_length=50)
    fecha_registro = models.DateField(default=timezone.now())
    foto = models.IntegerField()
    nombre_usuario = models.ForeignKey(Usuario, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)

class ConsultaMedica(models.Model):
    id = models.AutoField(primary_key=True);
    empleado = models.ForeignKey(Empleado, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())
    motivo = models.CharField(max_length=300, blank=True)
    problema_actual = models.CharField(max_length=300, blank=True)
    revision = models.CharField(max_length=300, blank=True)
    prescripcion = models.CharField(max_length=300, blank=True)
    examen_fisico = models.CharField(max_length=300, blank=True)

class AtencionEnfermeria(models.Model):
    empleado = models.ForeignKey(Empleado, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())
    motivo = models.CharField(max_length=300)
    diagnostico = models.CharField(max_length=300)
    plan_cuidados = models.CharField(max_length=500)

class SignosVitales(models.Model):
    consulta_medica = models.ForeignKey(ConsultaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    atencion_enfermeria = models.ForeignKey(AtencionEnfermeria, default = DEFAULT, blank=True, null=True, on_delete=models.CASCADE)
    presion_sistolica = models.IntegerField()
    presion_distolica = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.FloatField()

class PermisoMedico(models.Model):
    empleado = models.ForeignKey(Empleado, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField(default=timezone.now())
    dias = models.IntegerField()

class Enfermedad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

class Diagnostico(models.Model):
    permiso_medico = models.ForeignKey(PermisoMedico, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)

class Chequeo(models.Model):
    fecha = models.DateField(default=timezone.now())
    tipo = models.CharField(max_length=100)

class FichaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    chequeo = models.ForeignKey(Chequeo, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    foto = models.ImageField()

class AntecedentePatologicoPersonal(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    lugar_patologia = models.CharField(max_length=100)
    detalle_patologia = models.CharField(max_length=300)


class AparatoSistema(models.Model):
    nombre = models.CharField(max_length=100)
    hallazgo = models.CharField(max_length=300)
    detalle = models.CharField(max_length=300)


class RevisionAparatoSistema(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    aparato_sistema = models.ForeignKey(AparatoSistema, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)


class AntecedenteLaboral(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    edad_inicio = models.IntegerField()
    actividad = models.CharField(max_length=300)
    riesgos = models.CharField(max_length=300)
    epps = models.CharField(max_length=300)
    tiempo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

class Empresa(models.Model):
    antecedente_laboral = models.ForeignKey(AntecedenteLaboral, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    factores_riesgo = models.CharField(max_length=300)

class AntecedentePatologicoFamiliar(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=100)

class Inmunizacion(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=500)
    fecha_aplicacion = models.DateField(default=timezone.now())

class Vacuna(models.Model):
    inmunizacion = models.ForeignKey(Inmunizacion, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)

class ExamenLaboratorio(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    archivo = models.ImageField()

class SomaticoGeneral(models.Model):
    apariencia = models.CharField(max_length=300)
    estado_nutricional = models.CharField(max_length=300)
    actividades_psicomotoras = models.CharField(max_length=300)

class Regional(models.Model):
    piel_tegumentos = models.CharField(max_length=300)
    cabeza_cuello = models.CharField(max_length=300)
    torax = models.CharField(max_length=300)
    corazon = models.CharField(max_length=300)
    pulmones = models.CharField(max_length=300)
    abdomen = models.CharField(max_length=300)

class Columna(models.Model):
    cifosis_acentuada = models.BooleanField()
    contractura_muscular = models.BooleanField()
    dolor = models.BooleanField()
    lordosis_acentuada = models.BooleanField()
    escoliosis = models.BooleanField()
    motricidad = models.BooleanField()
    lassegue = models.BooleanField()
    detalle = models.CharField(max_length=300)

class RegionLumbar(models.Model):
    dolor_punio_percusion = models.BooleanField()
    motricidad = models.BooleanField()
    detalle = models.CharField(max_length=300)

class Extremidades(models.Model):
    phalen = models.BooleanField()
    tinel = models.BooleanField()
    dolor = models.BooleanField()
    signo_cajon_rodilla = models.BooleanField()
    finkelstein = models.BooleanField()
    motricidad = models.BooleanField()
    observaciones = models.CharField(max_length=500)

class ExamenFisico(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    signos_vitales = models.ForeignKey(SignosVitales, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    somatico_general = models.ForeignKey(SomaticoGeneral, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    regional = models.ForeignKey(Regional, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    columna = models.ForeignKey(Columna, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    region_lumbar = models.ForeignKey(RegionLumbar, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, blank=True, null=True, default = DEFAULT, on_delete=models.CASCADE)
    talla = models.FloatField()
    peso = models.FloatField()
    indice_masa_corporal = models.FloatField()