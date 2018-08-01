# Generated by Django 2.0 on 2018-08-01 00:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180731_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 670278, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 669452, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 667576, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 673196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 673162, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 671065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 1, 0, 24, 37, 674567, tzinfo=utc)),
        ),
    ]
