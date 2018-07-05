from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    contrasenia = models.CharField(max_length=16)

    def __str__(self):
        return "{}".format(self.usuario)

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
    ocupacion_act = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    foto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)

class ConsultaMedica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaConsulta = models.DateField()
    probActual = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    revision_medica = models.CharField(max_length=100)
    examen_fisico = models.CharField(max_length=100)

class AtencionEnfermeria(models.Model):
    fechaAtencion = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    motivoAtencion = models.CharField(max_length=100)
    diagnosticoEnfermeria = models.CharField(max_length=100)
    planCuidados = models.CharField(max_length=100)

class SignosVitales(models.Model):
    presion_sistolica = models.IntegerField()
    presion_distolica = models.IntegerField()
    pulso = models.IntegerField()
    temperatura = models.FloatField()
    consulta_medica = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)