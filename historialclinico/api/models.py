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
    ficha_actual = models.IntegerField(default = 0)

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
    TIPOS = (
        ('Inicial', 'Inicial'),
        ('Periódico', 'Periódico'),
        ('Postocupacional', 'Postocupacional'),
        ('Reintegro', 'Reintegro'),
    )
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    inmunizacion = models.ForeignKey(Inmunizacion, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='Periódico')

class AparatoSistema(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=300)

class AntecedentePatologicoPersonal(models.Model):
    LUGARES = (
        ('Sistema nervioso', 'Sistema nervioso'),
        ('Ojos', 'Ojos'),
        ('Oídos', 'Oídos'),
        ('Nariz', 'Nariz'),
        ('Garganta', 'Garganta'),
        ('Cardiovascular', 'Cardiovascular'),
        ('Respiratoria', 'Respiratoria'),
        ('Gastrointestinal', 'Gastrointestinal'),
        ('Metabólica', 'Metabólica'),
        ('Endocrina', 'Endocrina'),
        ('Renal', 'Renal'),
        ('Urinaria', 'Urinaria'),
        ('Órganos reproductores', 'Órganos reproductores'),
        ('Muscular', 'Muscular'),
        ('Articular', 'Articular'),
        ('Ósea (columna, otros)', 'Ósea (columna, otros)'),
        ('Piel y faneras', 'Piel y faneras'),
        ('Hematopoyéctica', 'Hematopoyéctica'),
        ('Sistema inmune (alergias)', 'Sistema inmune (alergias)'),
        ('Psiquiátrica', 'Psiquiátrica'),
        ('Cáncer - oncológicas', 'Cáncer - oncológicas'),
        ('Congénitas o genéticas', 'Congénitas o genéticas'),
        ('Traumática', 'Traumática'),
        ('Quirúrgica', 'Quirúrgica'),
        ('Medicamentos', 'Medicamentos')
    )
    ficha = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=100, choices=LUGARES, default="Ojos")
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
    TIPOS = (
        ('Físico', 'Físico'),
        ('Químico', 'Químico'),
        ('Biológico', 'Biológico'),
        ('Ergonómico', 'Ergonómico'),
        ('Mecánico', 'Mecánico'),
        ('Psicosocial', 'Psicosocial')
    )
    NOMBRES = (
        ('Físico',
            (
                ('Ruido', 'Ruido'),
                ('Vibración', 'Vibración'),
                ('Iluminación', 'Iluminación'),
                ('Radiaciones ionizantes', 'Radiaciones ionizantes'),
                ('Radiaciones no ionizantes', 'Radiaciones no ionizantes'),
                ('Presión', 'Presión'),
                ('Contacto con circuitos eléctricos', 'Contacto con circuitos eléctricos')
            )
        ),
        ('Químico',
            (
                ('Vapores', 'Vapores'),
                ('Gases (crudo, lixiviados, otros)', '(crudo, lixiviados, otros)'),
                ('Fibras (de madera, aluminio, otros)', 'Fibras (de madera, aluminio, otros)'),
                ('Polvos orgánicos', 'Polvos orgánicos'),
                ('Polvos inorgánicos', 'Polvos inorgánicos'),
                ('Humos metálicos (soldadura, otros)', 'Humos metálicos (soldadura, otros)'),
                ('Humos de combustión', 'Humos de combustión'),
                ('Neblinas', 'Neblinas'),
                ('Líquidos', 'Líquidos')
            )
        ),
        ('Biológico',
             (
                 ('Bacterias, hongos, virus, etc', 'Bacterias, hongos, virus, etc'),
                 ('Insalubridad en áreas', 'Insalubridad en áreas')
             )
        ),
        ('Ergonómico',
             (
                 ('Cargas', 'Cargas'),
                 ('Uso de pantallas de visualización', 'Uso de pantallas de visualización'),
                 ('Posturas en el trabajo mantenidas', 'Posturas en el trabajo mantenidas'),
                 ('Fatiga por esfuerzo físico', 'Fatiga por esfuerzo físico'),
                 ('Movimientos repetitivos', 'Movimientos repetitivos')
             )
        ),
        ('Mecánico',
             (
                 ('Contactos con superficies calientes', 'Contactos con superficies calientes'),
                 ('Contacto con herramientas, utensilios cortopunzantes', 'Contacto con herramientas, utensilios cortopunzantes'),
                 ('Golpes con objetos, herramientas', 'Golpes con objetos, herramientas'),
                 ('Atrapamiento en partes', 'Atrapamiento en partes'),
                 ('Caída de objetos', 'Caída de objetos'),
                 ('Derrumbes', 'Derrumbes'),
                 ('Transporte en vehículos - colisión', 'Transporte en vehículos - colisión')
             )
        ),
        ('Psicosocial',
             (
                 ('Medio ambiente físico de trabajo', 'Medio ambiente físico de trabajo'),
                 ('Factores propios de la tarea', 'Factores propios de la tarea'),
                 ('Organización del tiempo de trabajo', 'Organización del tiempo de trabajo'),
                 ('Gestión administrativa de la empresa', 'Gestión administrativa de la empresa')
             )
        )
    )
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    nombre = models.CharField(max_length=50, choices=NOMBRES)

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