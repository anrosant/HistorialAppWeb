# Generated by Django 2.1rc1 on 2018-08-12 16:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmunizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=15)),
                ('estadoCivil', models.CharField(max_length=20)),
                ('lugarNacimiento', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=80)),
                ('correo', models.EmailField(blank=True, max_length=30)),
                ('instruccion', models.CharField(blank=True, max_length=50)),
                ('profesion', models.CharField(blank=True, max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('ficha_actual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ciudad', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('Inicial', 'Inicial'), ('Periódico', 'Periódico'), ('Postocupacional', 'Postocupacional'), ('Reintegro', 'Reintegro')], default='Periódico', max_length=15)),
                ('prescripcion', models.CharField(blank=True, max_length=300)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
                ('inmunizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Inmunizacion')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteGinecoObstetrico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ultima_menstruacion', models.DateField()),
                ('planificacion_familiar', models.CharField(max_length=300)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedente', models.CharField(choices=[('Gesto', 'Gesto'), ('Parto', 'Parto'), ('Aborto', 'Aborto'), ('Cesárea', 'Cesárea')], default='Gesto', max_length=100)),
                ('antecedente_gineco_obstetrico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AntecedenteGinecoObstetrico')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('actividad', models.CharField(max_length=100)),
                ('epps', models.CharField(max_length=100)),
                ('area_trabajo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.CharField(max_length=50)),
                ('edad_inicio', models.CharField(max_length=20)),
                ('actividades_extralaborales', models.CharField(max_length=300)),
                ('actual', models.BooleanField(default=False)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedentePatologicoFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(max_length=100)),
                ('patologia', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=100)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examen_fisico', models.CharField(blank=True, max_length=300)),
                ('fechaConsulta', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('prescripcion', models.CharField(blank=True, max_length=300)),
                ('motivo', models.CharField(blank=True, max_length=300)),
                ('prob_actual', models.CharField(blank=True, max_length=300)),
                ('revision_medica', models.CharField(blank=True, max_length=300)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedentePatologicoPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(choices=[('Sistema nervioso', 'Sistema nervioso'), ('Ojos', 'Ojos'), ('Oídos', 'Oídos'), ('Nariz', 'Nariz'), ('Garganta', 'Garganta'), ('Cardiovascular', 'Cardiovascular'), ('Respiratoria', 'Respiratoria'), ('Gastrointestinal', 'Gastrointestinal'), ('Metabólica', 'Metabólica'), ('Endocrina', 'Endocrina'), ('Renal', 'Renal'), ('Urinaria', 'Urinaria'), ('Órganos reproductores', 'Órganos reproductores'), ('Muscular', 'Muscular'), ('Articular', 'Articular'), ('Ósea (columna, otros)', 'Ósea (columna, otros)'), ('Piel y faneras', 'Piel y faneras'), ('Hematopoyéctica', 'Hematopoyéctica'), ('Sistema inmune (alergias)', 'Sistema inmune (alergias)'), ('Psiquiátrica', 'Psiquiátrica'), ('Cáncer - oncológicas', 'Cáncer - oncológicas'), ('Congénitas o genéticas', 'Congénitas o genéticas'), ('Traumática', 'Traumática'), ('Quirúrgica', 'Quirúrgica'), ('Medicamentos', 'Medicamentos')], default='Ojos', max_length=100)),
                ('detalle', models.CharField(max_length=300)),
                ('ficha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
                ('consulta_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='AparatoSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Sistema nervioso', 'Sistema nervioso'), ('Órganos de los sentidos', 'Órganos de los sentidos'), ('Respiratorio', 'Respiratorio'), ('Digestivo', 'Digestivo'), ('Endócrino', 'Endócrino'), ('Músculo esquelético', 'Músculo esquelético'), ('Genital - urinario', 'Genital - urinario'), ('Piel y tegumentos', 'Piel y tegumentos'), ('Hemolinfático', 'Hemolinfático')], default='Digestivo', max_length=50)),
                ('detalle', models.CharField(max_length=300)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='AtencionEnfermeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivoAtencion', models.CharField(blank=True, max_length=300)),
                ('planCuidados', models.CharField(blank=True, max_length=500)),
                ('fechaAtencion', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('diagnosticoEnfermeria', models.CharField(blank=True, max_length=300)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Columna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cifosis_acentuada', models.BooleanField()),
                ('contractura_muscular', models.BooleanField()),
                ('dolor', models.BooleanField()),
                ('lordosis_acentuada', models.BooleanField()),
                ('escoliosis', models.BooleanField()),
                ('motricidad', models.CharField(blank=True, max_length=300)),
                ('lassegue', models.CharField(blank=True, max_length=300)),
                ('detalle_alteracion', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('grupo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEnfermedad', models.CharField(max_length=100)),
                ('consulta_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica')),
                ('ficha_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
                ('enfermedad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('consulta_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('presion_sistolica', models.IntegerField(blank=True)),
                ('presion_distolica', models.IntegerField(blank=True)),
                ('pulso', models.IntegerField(blank=True)),
                ('temperatura', models.FloatField(blank=True)),
                ('atencion_enfermeria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AtencionEnfermeria')),
                ('consulta_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica')),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='SomaticoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apariencia', models.CharField(blank=True, max_length=300)),
                ('estado_nutricional', models.CharField(blank=True, max_length=300)),
                ('actividades_psicomotoras', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Extremidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dolor', models.CharField(blank=True, max_length=20)),
                ('phalen', models.CharField(blank=True, max_length=20)),
                ('tinel', models.CharField(blank=True, max_length=20)),
                ('signo_cajon_rodilla', models.CharField(blank=True, max_length=20)),
                ('finkelstein', models.CharField(blank=True, max_length=20)),
                ('motricidad', models.CharField(blank=True, max_length=20)),
                ('observaciones', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piel_tegumentos', models.CharField(blank=True, max_length=300)),
                ('cabeza_cuello', models.CharField(blank=True, max_length=300)),
                ('torax', models.CharField(blank=True, max_length=300)),
                ('corazon', models.CharField(blank=True, max_length=300)),
                ('pulmones', models.CharField(blank=True, max_length=300)),
                ('abdomen', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RegionLumbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dolor_punio_percusion', models.BooleanField()),
                ('motricidad', models.BooleanField()),
                ('detalle_alteracion', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.FloatField()),
                ('peso', models.FloatField()),
                ('indice_masa_corporal', models.FloatField()),
                ('examen_neurologico_elemental', models.CharField(blank=True, max_length=300)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
                ('signos_vitales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SignosVitales')),
                ('somatico_general', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SomaticoGeneral')),
                ('columna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Columna')),
                ('region_lumbar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.RegionLumbar')),
                ('extremidades', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Extremidades')),
                ('regional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Regional')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenLaboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Laboratorio', 'Laboratorio'), ('Emo', 'Emo'), ('Coproparasitario', 'Coproparasitario'), ('Pruebas especiales de laboratorio', 'Pruebas especiales de laboratorio'), ('Oftalmología', 'Oftalmología'), ('Espirometría', 'Espirometría')], default='Laboratorio', max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='FactorRiesgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Físico', 'Físico'), ('Químico', 'Químico'), ('Biológico', 'Biológico'), ('Ergonómico', 'Ergonómico'), ('Mecánico', 'Mecánico'), ('Psicosocial', 'Psicosocial')], max_length=50)),
                ('nombre', models.CharField(choices=[('Físico', (('Ruido', 'Ruido'), ('Vibración', 'Vibración'), ('Iluminación', 'Iluminación'), ('Radiaciones ionizantes', 'Radiaciones ionizantes'), ('Radiaciones no ionizantes', 'Radiaciones no ionizantes'), ('Presión', 'Presión'), ('Contacto con circuitos eléctricos', 'Contacto con circuitos eléctricos'))), ('Químico', (('Vapores', 'Vapores'), ('Gases (crudo, lixiviados, otros)', '(crudo, lixiviados, otros)'), ('Fibras (de madera, aluminio, otros)', 'Fibras (de madera, aluminio, otros)'), ('Polvos orgánicos', 'Polvos orgánicos'), ('Polvos inorgánicos', 'Polvos inorgánicos'), ('Humos metálicos (soldadura, otros)', 'Humos metálicos (soldadura, otros)'), ('Humos de combustión', 'Humos de combustión'), ('Neblinas', 'Neblinas'), ('Líquidos', 'Líquidos'))), ('Biológico', (('Bacterias, hongos, virus, etc', 'Bacterias, hongos, virus, etc'), ('Insalubridad en áreas', 'Insalubridad en áreas'))), ('Ergonómico', (('Cargas', 'Cargas'), ('Uso de pantallas de visualización', 'Uso de pantallas de visualización'), ('Posturas en el trabajo mantenidas', 'Posturas en el trabajo mantenidas'), ('Fatiga por esfuerzo físico', 'Fatiga por esfuerzo físico'), ('Movimientos repetitivos', 'Movimientos repetitivos'))), ('Mecánico', (('Contactos con superficies calientes', 'Contactos con superficies calientes'), ('Contacto con herramientas, utensilios cortopunzantes', 'Contacto con herramientas, utensilios cortopunzantes'), ('Golpes con objetos, herramientas', 'Golpes con objetos, herramientas'), ('Atrapamiento en partes', 'Atrapamiento en partes'), ('Caída de objetos', 'Caída de objetos'), ('Derrumbes', 'Derrumbes'), ('Transporte en vehículos - colisión', 'Transporte en vehículos - colisión'))), ('Psicosocial', (('Medio ambiente físico de trabajo', 'Medio ambiente físico de trabajo'), ('Factores propios de la tarea', 'Factores propios de la tarea'), ('Organización del tiempo de trabajo', 'Organización del tiempo de trabajo'), ('Gestión administrativa de la empresa', 'Gestión administrativa de la empresa')))], max_length=50)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Habito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcohol', models.CharField(choices=[('De 2 a 12 veces al año', 'De 2 a 12 veces al año'), ('Una vez al año', 'Una vez al año'), ('De 5 a 7 días a la semana', 'De 5 a 7 días a la semana'), ('De 2 a 4 veces a la semana', 'De 2 a 4 veces a la semana'), ('De 2 a 7 veces a la semana', 'De 2 a 7 veces a la semana'), ('Al menos una vez a la semana', 'Al menos una vez a la semana'), ('No consume', 'No consume')], default='No consume', max_length=100)),
                ('tabaco', models.CharField(choices=[('1 o 2 veces al año', '1 o 2 veces al año'), ('3 veces al mes', '3 veces al mes'), ('4 veces a la semana', '4 veces a la semana'), ('A diario o casi a diario', 'A diario o casi a diario'), ('Ex-fumador', 'Ex-fumador'), ('No fuma', 'No fuma')], default='No fuma', max_length=100)),
                ('cantidad_tabaco', models.IntegerField(default=0)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(blank=True, max_length=20)),
                ('columna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Columna')),
                ('extremidades', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Extremidades')),
            ],
        ),
        migrations.CreateModel(
            name='PermisoMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('doctor', models.CharField(blank=True, max_length=100)),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('fecha_fin', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('dias_permiso', models.IntegerField()),
                ('observaciones_permiso', models.CharField(blank=True, max_length=100)),
                ('consulta_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica')),
                ('diagnostico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Diagnostico')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=200)),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Empleado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, choices=[('Tétanos', 'Tétanos'), ('Hepatitis A - B', 'Hepatitis A - B'), ('Fiebre tifoidea', 'Fiebre tifoidea'), ('Fiebre amarilla', 'Fiebre amarilla')], default='Tétanos', max_length=30)),
                ('dosis', models.CharField(blank=True, choices=[('Primera', 'Primera'), ('Segunda', 'Segunda'), ('Tercera', 'Tercera'), ('Refuerzo', 'Refuerzo')], default='Primera', max_length=15)),
                ('fecha', models.DateField(default=datetime.datetime(2018, 8, 12, 16, 34, 50, 444166, tzinfo=utc))),
                ('inmunizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Inmunizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerabilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_vulnerable', models.BooleanField(default=False)),
                ('persona_discapacidad', models.BooleanField(default=False)),
                ('descripcion', models.CharField(blank=True, max_length=300)),
                ('ficha_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.FichaMedica')),
            ],
        ),
    ]
