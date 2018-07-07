from django.db import models

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
    fecha_nacimiento = models.DateField()
    ocupacion_actual = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    foto = models.IntegerField()
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)

class ConsultaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=300)
    problema_actual = models.CharField(max_length=300)
    revision = models.CharField(max_length=300)
    prescripcion = models.CharField(max_length=300)
    examen_fisico = models.CharField(max_length=300)

class AtencionEnfermeria(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=300)
    diagnostico = models.CharField(max_length=300)
    plan_cuidados = models.CharField(max_length=500)

class SignosVitales(models.Model):
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    atencion_enfermeria = models.ForeignKey(AtencionEnfermeria, on_delete=models.CASCADE)
    presion_sistolica = models.IntegerField()
    presion_distolica = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.FloatField()

class PermisoMedico(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dias = models.IntegerField()

class Enfermedad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

class Diagnostico(models.Model):
    permiso_medico = models.ForeignKey(PermisoMedico, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)

class Chequeo(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=100)

class FichaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    chequeo = models.ForeignKey(Chequeo, on_delete=models.CASCADE)
    foto = models.ImageField()

class AntecedentePatologicoPersonal(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    lugar_patologia = models.CharField(max_length=100)
    detalle_patologia = models.CharField(max_length=300)

class RevisionAparatoSistema(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)

class AparatoSistema(models.Model):
    revision_aparato_sistema = models.ForeignKey(RevisionAparatoSistema, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    hallazgo = models.CharField(max_length=300)
    detalle = models.CharField(max_length=300)

class AntecedenteLaboral(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    edad_inicio = models.IntegerField()
    actividad = models.CharField(max_length=300)
    riesgos = models.CharField(max_length=300)
    epps = models.CharField(max_length=300)
    tiempo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

class Empresa(models.Model):
    antecedente_laboral = models.ForeignKey(AntecedenteLaboral, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    factores_riesgo = models.CharField(max_length=300)

class AntecedentePatologicoFamiliar(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=100)

class Inmunizacion(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=500)
    fecha_aplicacion = models.DateField()

class Vacuna(models.Model):
    inmunizacion = models.ForeignKey(Inmunizacion, on_delete=models.CASCADE)
    nombre = models.CharField()
    numero = models.CharField()

class ExamenLaboratorio(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    descripcion = models.CharField()
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
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    signos_vitales = models.ForeignKey(SignosVitales, on_delete=models.CASCADE)
    somatico_general = models.ForeignKey(SomaticoGeneral, on_delete=models.CASCADE)
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    columna = models.ForeignKey(Columna, on_delete=models.CASCADE)
    region_lumbar = models.ForeignKey(RegionLumbar, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, on_delete=models.CASCADE)
    talla = models.FloatField()
    peso = models.FloatField()
    indice_masa_corporal = models.FloatField()