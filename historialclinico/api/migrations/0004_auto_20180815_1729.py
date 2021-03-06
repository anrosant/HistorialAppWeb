# Generated by Django 2.0 on 2018-08-15 17:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180815_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 882739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 881548, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 878859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fichamedica',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 887584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 889028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 888978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 888876, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 883925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 15, 17, 29, 6, 886621, tzinfo=utc)),
        ),
    ]
