'''from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import *

# Test para consulta médica
class ConsultaMedicaTestCase(TestCase):
    def setUp(self):
        usuario = User()
        usuario.username = "ejemplouser"
        usuario.password = "us1234er"
        usuario.save()

        empleado = Empleado()

        empleado.foto = "http://historialmedico.pythonanywhere.com/media/img001_idaZQQT.jpg"
        empleado.cedula = "0985462350"
        empleado.nombre = "Carla"
        empleado.apellido = "Garcia"
        empleado.edad = 30
        empleado.sexo = "Femenino"
        empleado.estadoCivil = "Casada"
        empleado.lugarNacimiento = "Manabí"
        empleado.fechaNacimiento = "1983-06-04"
        empleado.direccion = "La FAE"
        empleado.correo = ""
        empleado.instruccion = "Superior"
        empleado.profesion = "Enfermera"
        empleado.ocupacion = "Enfermera"
        empleado.fechaRegistro = "2018-07-30"
        empleado.ficha_actual = 2
        empleado.save()

        consulta = ConsultaMedica()
        consulta.empleado=empleado
        consulta.examen_fisico="ninguno"
        consulta.fechaConsulta = "2018-05-11"
        consulta.prescripcion = "Descansar"
        consulta.motivo = "Cansancio"
        consulta.prob_actual ="Estrés"
        consulta.revision_medica = "ninguna"
        consulta.save()


        """Define the test client and other test variables."""
        user = User.objects.get(username='ejemplouser')
        self.client = APIClient()
        self.client.force_authenticate(user)

        self.consulta_data = {
                                "empleado": 1,
                                "examen_fisico": "No refiere",
                                "fechaConsulta": "2018-06-11",
                                "prescripcion": " ",
                                "motivo": "Dolor de cabeza ",
                                "prob_actual": "ninguno",
                                "revision_medica": "ninguna"
                            }

        self.response = self.client.post(
            reverse('api:createconsulta'),
            self.consulta_data,
            format='json')

    def test_crear_consulta(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_consulta(self):
        response = self.client.get(
            reverse('api:createconsulta'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_consulta(self):
        consulta = ConsultaMedica.objects.get(pk = 1)
        nueva_consulta = {
                                "empleado": 1,
                                "examen_fisico": "No refiere",
                                "fechaConsulta": "2018-05-10",
                                "prescripcion": " ",
                                "motivo": "Dolor de cabeza ",
                                "prob_actual": "ninguno",
                                "revision_medica": "ninguna"
                            }
        res = self.client.put(
            reverse('api:consultadetails', kwargs={'pk': consulta.id}),
            nueva_consulta, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_eliminar_consulta(self):
        consulta = ConsultaMedica.objects.get(pk = 1)
        response = self.client.delete(
            reverse('api:consultadetails', kwargs={'pk': consulta.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

# Test para atención enfermería
class AtencionEnfermeriaTestCase(TestCase):
    def setUp(self):
        usuario = User()
        usuario.username = "ejemplouser"
        usuario.password = "us1234er"
        usuario.save()

        empleado = Empleado()

        empleado.foto = "http://historialmedico.pythonanywhere.com/media/img001_idaZQQT.jpg"
        empleado.cedula = "0985462350"
        empleado.nombre = "Carla"
        empleado.apellido = "Garcia"
        empleado.edad = 30
        empleado.sexo = "Femenino"
        empleado.estadoCivil = "Casada"
        empleado.lugarNacimiento = "Manabí"
        empleado.fechaNacimiento = "1983-06-04"
        empleado.direccion = "La FAE"
        empleado.correo = ""
        empleado.instruccion = "Superior"
        empleado.profesion = "Enfermera"
        empleado.ocupacion = "Enfermera"
        empleado.fechaRegistro = "2018-07-30"
        empleado.ficha_actual = 2
        empleado.save()

        atencion = AtencionEnfermeria()

        atencion.empleado=empleado
        atencion.motivoAtencion="dolor de espalda"
        atencion.planCuidados = "Descanso"
        atencion.fechaAtencion = "2018-05-11"
        atencion.diagnosticoEnfermeria = "Cansancio"
        atencion.save()


        """Define the test client and other test variables."""
        user = User.objects.get(username='ejemplouser')
        self.client = APIClient()
        self.client.force_authenticate(user)

        self.atencion_data = {
                                "empleado": 1,
                                "motivoAtencion": "dolor de espalda",
                                "planCuidados": "Descanso",
                                "fechaAtencion": "2018-06-11",
                                "diagnosticoEnfermeria": "Cansancio"
                            }

        self.response = self.client.post(
            reverse('api:createatencion'),
            self.atencion_data,
            format='json')

    def test_crear_atencion(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_atencion(self):
        response = self.client.get(
            reverse('api:createatencion'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_atencion(self):
        atencion = AtencionEnfermeria.objects.get(pk = 1)
        nueva_atencion = {
                                "empleado": 1,
                                "examen_fisico": "No refiere",
                                "fechaConsulta": "2018-07-02",
                                "prescripcion": " ",
                                "motivo": "Dolor de cabeza ",
                                "prob_actual": "",
                                "revision_medica": "ninguna"
                            }
        res = self.client.put(
            reverse('api:atenciondetails', kwargs={'pk': atencion.id}),
            nueva_atencion, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_eliminar_atencion(self):
        atencion = AtencionEnfermeria.objects.get(pk = 1)
        response = self.client.delete(
            reverse('api:atenciondetails', kwargs={'pk': atencion.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

# Test para signos vitales
class SignosVitalesTestCase(TestCase):
    def setUp(self):
        usuario = User()
        usuario.username = "ejemplouser"
        usuario.password = "us1234er"
        usuario.save()

        empleado = Empleado()
        empleado.foto = "http://historialmedico.pythonanywhere.com/media/img001_idaZQQT.jpg"
        empleado.cedula = "0985462350"
        empleado.nombre = "Carla"
        empleado.apellido = "Garcia"
        empleado.edad = 30
        empleado.sexo = "Femenino"
        empleado.estadoCivil = "Casada"
        empleado.lugarNacimiento = "Manabí"
        empleado.fechaNacimiento = "1983-06-04"
        empleado.direccion = "La FAE"
        empleado.correo = ""
        empleado.instruccion = "Superior"
        empleado.profesion = "Enfermera"
        empleado.ocupacion = "Enfermera"
        empleado.fechaRegistro = "2018-07-30"
        empleado.ficha_actual = 2
        empleado.save()

        atencion = AtencionEnfermeria()

        atencion.empleado=empleado
        atencion.motivoAtencion="dolor de espalda"
        atencion.planCuidados = "Descanso"
        atencion.fechaAtencion = "2018-05-11"
        atencion.diagnosticoEnfermeria = "Cansancio"
        atencion.save()

        signos = SignosVitales()
        signos.empleado = empleado
        signos.atencion_enfermeria = atencion
        signos.fecha = "2018-07-12"
        signos.presion_sistolica = 120
        signos.presion_distolica = 89
        signos.pulso = 95
        signos.temperatura = 37.8
        signos.save()

        user = User.objects.get(username='ejemplouser')
        self.client = APIClient()
        self.client.force_authenticate(user)

        self.signos_data = {
                                "empleado": 1,
                                "consulta_medica": "",
                                "atencion_enfermeria": 1,
                                "fecha": "2018-08-11",
                                "presion_sistolica": 122,
                                "presion_distolica":88,
                                "pulso": 93,
                                "temperatura": 38
                            }

        self.response = self.client.post(
            reverse('api:createsignos'),
            self.signos_data,
            format='json')

    def test_crear_signos(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_signos(self):
        response = self.client.get(
            reverse('api:createsignos'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_signos(self):
        signos = AtencionEnfermeria.objects.get(pk = 1)
        nuevo_signo = {
                                "empleado": 1,
                                "consulta_medica": "",
                                "atencion_enfermeria": 1,
                                "fecha": "2018-08-11",
                                "presion_sistolica": 122,
                                "presion_distolica":81,
                                "pulso": 88,
                                "temperatura": 38
                            }
        res = self.client.put(
            reverse('api:signosdetails', kwargs={'pk': signos.id}),
            nuevo_signo, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_eliminar_signos(self):
        signos = SignosVitales.objects.get(pk = 1)
        response = self.client.delete(
            reverse('api:signosdetails', kwargs={'pk': signos.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

# Test para efermedad
class EnfermedadTestCase(TestCase):
    def setUp(self):
        usuario = User()
        usuario.username = "ejemplouser"
        usuario.password = "us1234er"
        usuario.save()

        enfermedad = Enfermedad()
        enfermedad.codigo="A00"
        enfermedad.nombre="Cólera"
        enfermedad.grupo="|I1"

        """Define the test client and other test variables."""
        user = User.objects.get(username='ejemplouser')
        self.client = APIClient()
        self.client.force_authenticate(user)

        self.enfermedad_data = {"codigo": "C1",
                                "nombre": "Rayos x",
                                "grupo": "G1"
                                }

        self.response = self.client.post(
            reverse('api:createenfermedad'),
            self.enfermedad_data,
            format="json")

    def test_crear_enfermedad(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_enfermedades(self):
        response = self.client.get(
            reverse('api:createenfermedad'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_enfermedad(self):
        enfermedad = Enfermedad.objects.get()
        nueva_enfermedad = {"codigo": "A01",
                            "nombre": "Rayos x",
                            "grupo": "G1"
                            }
        res = self.client.put(
            reverse('api:enfermedaddetails', kwargs={'pk': enfermedad.id}),
            nueva_enfermedad, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_eliminar_enfermedad(self):
        enfermedad = Enfermedad.objects.get()
        response = self.client.delete(
            reverse('api:enfermedaddetails', kwargs={'pk': enfermedad.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

# Test para diagnostico
class DiagnosticoTestCase(TestCase):
    def setUp(self):
        usuario = User()
        usuario.username = "ejemplouser"
        usuario.password = "us1234er"
        usuario.save()

        enfermedad = Enfermedad()
        enfermedad.codigo = "A00"
        enfermedad.nombre = "Cólera"
        enfermedad.grupo = "|I1"
        enfermedad.save()

        empleado = Empleado()
        empleado.foto = "http://historialmedico.pythonanywhere.com/media/img001_idaZQQT.jpg"
        empleado.cedula = "0985462350"
        empleado.nombre = "Carla"
        empleado.apellido = "Garcia"
        empleado.edad = 30
        empleado.sexo = "Femenino"
        empleado.estadoCivil = "Casada"
        empleado.lugarNacimiento = "Manabí"
        empleado.fechaNacimiento = "1983-06-04"
        empleado.direccion = "La FAE"
        empleado.correo = ""
        empleado.instruccion = "Superior"
        empleado.profesion = "Enfermera"
        empleado.ocupacion = "Enfermera"
        empleado.fechaRegistro = "2018-07-30"
        empleado.ficha_actual = 2
        empleado.save()

        consulta = ConsultaMedica()
        consulta.empleado = empleado
        consulta.examen_fisico = "ninguno"
        consulta.fechaConsulta = "2018-05-11"
        consulta.prescripcion = "Descansar"
        consulta.motivo = "Cansancio"
        consulta.prob_actual = "Estrés"
        consulta.revision_medica = "ninguna"
        consulta.save()

        diagnostico = Diagnostico()
        diagnostico.enfermedad=enfermedad
        diagnostico.consulta_medica=consulta
        diagnostico.tipoEnfermedad="crónica"
        diagnostico.save()

        """Define the test client and other test variables."""
        user = User.objects.get(username='ejemplouser')
        self.client = APIClient()
        self.client.force_authenticate(user)

        self.diagnostico_data = {"enfermedad": 1,
                                "consulta_medica": 1,
                                "tipoEnfermedad": "ninguno"
                                 }

        self.response = self.client.post(
            reverse('api:creatediagnostico'),
            self.diagnostico_data,
            format="json")

    def test_crear_diagnostico(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_diagnostico(self):
        response = self.client.get(
            reverse('api:creatediagnostico'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_diagnostico(self):
        diagnostico = Diagnostico.objects.get(pk = 1)
        nuevo_diagnostico = {
                                "enfermedad": 1,
                                "consulta_medica": 1,
                                "tipoEnfermedad": "leve"
                            }
        res = self.client.put(
            reverse('api:diagnosticodetails', kwargs={'pk': diagnostico.id}),
            nuevo_diagnostico, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_eliminar_diagnostico(self):
        diagnostico = Diagnostico.objects.get(pk = 1)
        response = self.client.delete(
            reverse('api:diagnosticodetails', kwargs={'pk': diagnostico.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)