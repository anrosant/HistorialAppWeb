from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Define this after the ModelTestCase
class ConsultaMedicaTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.get(username='historial')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.consulta_medica_data = {'empleado': '1', 'examen_fisico': 'Rayos x', 'fechaConsulta': '2018-08-01',
                                     'motivo': 'Dolor de pierna', 'prob_actual':'','revision_medica': 'Algo'}
        self.response = self.client.post(
            reverse('api:create'),
            self.consulta_medica_data,
            format="json")

    def test_crear_consulta_medica(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)