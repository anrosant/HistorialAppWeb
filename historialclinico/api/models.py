from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Empleado(models.Model):
    foto = models.ImageField()
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15)
    estadoCivil = models.CharField(max_length=20)
    lugarNacimiento = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, max_length=30)
    instruccion = models.CharField(max_length=30)
    profesion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    fechaRegistro = models.DateField(default=timezone.now())

    def __str__(self):
        return "{}".format(self.nombre)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null = True)
    token = models.CharField(max_length=200, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

class ConsultaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    examen_fisico = models.CharField(max_length=300)
    fechaConsulta = models.DateField(default=timezone.now())
    prescripcion = models.CharField(max_length=300, blank=True)
    motivo = models.CharField(max_length=300, blank=True)
    prob_actual = models.CharField(max_length=300, blank=True)
    revision_medica = models.CharField(max_length=300, blank=True)

class AtencionEnfermeria(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    motivoAtencion = models.CharField(max_length=300, blank=True)
    planCuidados = models.CharField(max_length=500, blank=True)
    fechaAtencion = models.DateField(default=timezone.now())
    diagnosticoEnfermeria = models.CharField(max_length=300, blank=True)

class SignosVitales(models.Model):
    empleado = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    atencion_enfermeria = models.ForeignKey(AtencionEnfermeria, null=True, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())
    presion_sistolica = models.IntegerField()
    presion_distolica = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.FloatField()

class Enfermedad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)

class Diagnostico(models.Model):
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    tipoEnfermedad = models.CharField(max_length=100)

class PermisoMedico(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField(default=timezone.now())
    dias_permiso = models.IntegerField()
    observaciones_permiso = models.CharField(max_length=100)

class Inmunizacion(models.Model):
    observacion = models.CharField(max_length=300)

class Vacuna(models.Model):
    inmunizacion = models.ForeignKey(Inmunizacion, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    dosis = models.IntegerField()
    fecha = models.DateField(default=timezone.now())

class FichaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    inmunizacion = models.ForeignKey(Inmunizacion, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15)

class AparatoSistema(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=300)

class AntecedentePatologicoPersonal(models.Model):
    ficha = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=100)
    detalle = models.CharField(max_length=300)

class AntecedentePatologicoFamiliar(models.Model):
    ficha = models.ForeignKey(FichaMedica, null=False, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=100)
    patologia = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    actividad = models.CharField(max_length=100)
    epps = models.CharField(max_length=100)

class AntecedenteLaboral(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.CASCADE)
    tiempo = models.CharField(max_length=50)
    edad_inicio = models.CharField(max_length=2)
    actual = models.BooleanField(default=False)

class FactorRiesgo(models.Model):
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

class ExamenLaboratorio(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField()

class SomaticoGeneral(models.Model):
    apariencia = models.CharField(max_length=300, blank=True)
    estado_nutricional = models.CharField(max_length=300, blank=True)
    actividades_psicomotoras = models.CharField(max_length=300, blank=True)

class Regional(models.Model):
    piel_tegumentos = models.CharField(max_length=300, blank=True)
    cabeza_cuello = models.CharField(max_length=300, blank=True)
    torax = models.CharField(max_length=300, blank=True)
    corazon = models.CharField(max_length=300, blank=True)
    pulmones = models.CharField(max_length=300, blank=True)
    abdomen = models.CharField(max_length=300, blank=True)

class Columna(models.Model):
    cifosis_acentuada = models.BooleanField()
    contractura_muscular = models.BooleanField()
    dolor = models.BooleanField()
    lordosis_acentuada = models.BooleanField()
    escoliosis = models.BooleanField()
    motricidad = models.CharField(max_length=300, blank=True)
    lassegue = models.CharField(max_length=300, blank=True)
    detalle_alteracion = models.CharField(max_length=300, blank=True)

class Lumbar(models.Model):
    dolor_punio_percusion = models.BooleanField()
    motricidad = models.BooleanField()
    detalle_alteracion = models.CharField(max_length=300, blank=True)

class Extremidades(models.Model):
    dolor = models.CharField(max_length=20, blank=True)
    phalen = models.CharField(max_length=20, blank=True)
    tinel = models.CharField(max_length=20, blank=True)
    signo_cajon_rodilla = models.CharField(max_length=20, blank=True)
    finkelstein = models.CharField(max_length=20, blank=True)
    motricidad = models.CharField(max_length=20, blank=True)
    observaciones = models.CharField(max_length=20, blank=True)

class Localizacion(models.Model):
    columna = models.ForeignKey(Columna, null=True, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, null=True, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=20, blank=True)

class ExamenFisico(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    signos_vitales = models.ForeignKey(SignosVitales, null=True, on_delete=models.CASCADE)
    somatico_general = models.ForeignKey(SomaticoGeneral, null=True, on_delete=models.CASCADE)
    columna = models.ForeignKey(Columna, null=True, on_delete=models.CASCADE)
    lumbar = models.ForeignKey(Lumbar, null=True, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, null=True, on_delete=models.CASCADE)
    regional = models.ForeignKey(Regional, null=True, on_delete=models.CASCADE)
    talla = models.FloatField()
    peso = models.FloatField()
    indice_masa_corporal = models.FloatField()