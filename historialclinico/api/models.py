from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Empleado(models.Model):
    foto = models.ImageField()
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15)
    estadoCivil = models.CharField(max_length=20)
    lugarNacimiento = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=80)
    correo = models.EmailField(blank=True, max_length=30)
    instruccion = models.CharField(blank=True, max_length=50)
    profesion = models.CharField(blank=True, max_length=50)
    ocupacion = models.CharField(max_length=50)
    fechaRegistro = models.DateField(default=timezone.now())
    ficha_actual = models.IntegerField(default = 0)

    def __str__(self):
        return "{}".format(self.nombre)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null = True)
    token = models.CharField(max_length=200, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class ConsultaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    examen_fisico = models.CharField(max_length=300, blank = True)
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
    presion_sistolica = models.IntegerField(null=True)
    presion_distolica = models.IntegerField(null=True)
    pulso = models.IntegerField(null=True)
    temperatura = models.FloatField(null=True)

class Enfermedad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)

class Inmunizacion(models.Model):
    observacion = models.CharField(max_length=300)

class Vacuna(models.Model):
    NOMBRES = (
        ('Tétanos', 'Tétanos'),
        ('Hepatitis A - B', 'Hepatitis A - B'),
        ('Fiebre tifoidea', 'Fiebre tifoidea'),
        ('Fiebre amarilla', 'Fiebre amarilla')
    )
    DOSIS = (
        ('Primera', 'Primera'),
        ('Segunda', 'Segunda'),
        ('Tercera', 'Tercera'),
        ('Refuerzo', 'Refuerzo')
    )
    inmunizacion = models.ForeignKey(Inmunizacion, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, choices=NOMBRES, default='Tétanos', blank=True)
    dosis = models.CharField(max_length=15, choices=DOSIS, default='Primera', blank=True)
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
    fecha = models.DateField(default=timezone.now())
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15, choices=TIPOS, default='Periódico')
    prescripcion = models.CharField(max_length=300, blank=True)

class PermisoMedico(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    fecha_registro = models.DateField(default=timezone.now())
    doctor = models.CharField(max_length=100, blank = True)
    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField(default=timezone.now())
    dias_permiso = models.IntegerField()
    observaciones_permiso = models.CharField(max_length=100, blank = True)

class Diagnostico(models.Model):
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    consulta_medica = models.ForeignKey(ConsultaMedica, null=True, on_delete=models.CASCADE)
    ficha_medica = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    tipoEnfermedad = models.CharField(max_length=100)
    permiso_medico = models.ForeignKey(PermisoMedico, null=True, on_delete=models.CASCADE)

class AparatoSistema(models.Model):
    NOMBRES = (
        ('Sistema nervioso', 'Sistema nervioso'),
        ('Órganos de los sentidos', 'Órganos de los sentidos'),
        ('Respiratorio', 'Respiratorio'),
        ('Digestivo', 'Digestivo'),
        ('Endócrino', 'Endócrino'),
        ('Músculo esquelético', 'Músculo esquelético'),
        ('Genital - urinario', 'Genital - urinario'),
        ('Piel y tegumentos', 'Piel y tegumentos'),
        ('Hemolinfático', 'Hemolinfático'),
    )
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, choices=NOMBRES, default='Digestivo')
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

class AntecedenteGinecoObstetrico(models.Model):
    ficha = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    fecha_ultima_menstruacion = models.DateField()
    planificacion_familiar = models.CharField(max_length=300)

class Antecedente(models.Model):
    ANTECEDENTES = (
        ('Gesto', 'Gesto'),
        ('Parto', 'Parto'),
        ('Aborto', 'Aborto'),
        ('Cesárea', 'Cesárea')
    )
    antecedente_gineco_obstetrico = models.ForeignKey(AntecedenteGinecoObstetrico, on_delete=models.CASCADE)
    antecedente = models.CharField(max_length=100, choices=ANTECEDENTES, default="Gesto")

class Habito(models.Model):
    ALCOHOL = (
        ('De 2 a 12 veces al año', 'De 2 a 12 veces al año'),
        ('Una vez al año', 'Una vez al año'),
        ('De 5 a 7 días a la semana', 'De 5 a 7 días a la semana'),
        ('De 2 a 4 veces a la semana', 'De 2 a 4 veces a la semana'),
        ('De 2 a 7 veces a la semana', 'De 2 a 7 veces a la semana'),
        ('Al menos una vez a la semana', 'Al menos una vez a la semana'),
        ('No consume', 'No consume')
    )
    TABACO = (
        ('1 o 2 veces al año', '1 o 2 veces al año'),
        ('3 veces al mes', '3 veces al mes'),
        ('4 veces a la semana', '4 veces a la semana'),
        ('A diario o casi a diario', 'A diario o casi a diario'),
        ('Ex-fumador', 'Ex-fumador'),
        ('No fuma', 'No fuma')
    )
    ficha = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    alcohol = models.CharField(max_length=100, choices=ALCOHOL, null=True, default="No consume")
    tabaco = models.CharField(max_length=100, choices=TABACO, null=True, default="No fuma")
    cantidad_tabaco = models.IntegerField(null=True)

class AntecedentePatologicoFamiliar(models.Model):
    ficha = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=100)
    patologia = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    #riesgos = models.CharField(blank=True, null=True, max_length=300)
    epps = models.CharField(blank=True, max_length=100)
    area_trabajo = models.CharField(max_length=100)

class AntecedenteLaboral(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tiempo = models.CharField(max_length=50)
    edad_inicio = models.CharField(max_length=20)
    actividades_extralaborales = models.CharField(max_length=300)
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
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    nombre = models.CharField(max_length=50, choices=NOMBRES)

class ExamenConsulta(models.Model):
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    imagen = models.ImageField()

class ExamenLaboratorio(models.Model):
    EXAMENES = (
        ('Laboratorio', 'Laboratorio'),
        ('Emo', 'Emo'),
        ('Coproparasitario', 'Coproparasitario'),
        ('Pruebas especiales de laboratorio', 'Pruebas especiales de laboratorio'),
        ('Oftalmología', 'Oftalmología'),
        ('Espirometría', 'Espirometría')
    )
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=EXAMENES, default='Laboratorio')
    descripcion = models.CharField(max_length=500, blank = True)
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
    cifosis_acentuada = models.NullBooleanField(null=True)
    contractura_muscular = models.NullBooleanField(null=True)
    dolor = models.NullBooleanField(null=True)
    lordosis_acentuada = models.NullBooleanField(null=True)
    escoliosis = models.NullBooleanField(null=True)
    motricidad = models.CharField(max_length=20, null=True)
    detalle_alteracion = models.CharField(max_length=300, blank=True)

class RegionLumbar(models.Model):
    dolor_punio_percusion = models.NullBooleanField(null=True)
    motricidad = models.CharField(max_length=20, null=True)
    detalle_alteracion = models.CharField(max_length=300, blank=True, null = True)

class Extremidades(models.Model):
    dolor = models.NullBooleanField(null=True)
    motricidad = models.CharField(max_length=20, null=True)
    observaciones = models.CharField(max_length=20, blank=True)

class Localizacion(models.Model):
    columna = models.ForeignKey(Columna, null=True, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, null=True, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=40, blank=True)
    lugar = models.CharField(max_length=20, blank=True)

class ExamenFisico(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    signos_vitales = models.ForeignKey(SignosVitales, null=True, on_delete=models.CASCADE)
    somatico_general = models.ForeignKey(SomaticoGeneral, null=True, on_delete=models.CASCADE)
    columna = models.ForeignKey(Columna, null=True, on_delete=models.CASCADE)
    region_lumbar = models.ForeignKey(RegionLumbar, null=True, on_delete=models.CASCADE)
    extremidades = models.ForeignKey(Extremidades, null=True, on_delete=models.CASCADE)
    regional = models.ForeignKey(Regional, null=True, on_delete=models.CASCADE)
    talla = models.FloatField(null=True)
    peso = models.FloatField(null=True)
    indice_masa_corporal = models.FloatField(null=True)
    frecuencia_respiratoria = models.IntegerField(null=True)
    examen_neurologico_elemental = models.CharField(max_length=300, blank=True)

class Vulnerabilidad(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, null=True, on_delete=models.CASCADE)
    persona_vulnerable = models.NullBooleanField(default=False, null=True)
    persona_discapacidad = models.NullBooleanField(default=False, null=True)
    descripcion = models.CharField(max_length=300, blank=True)