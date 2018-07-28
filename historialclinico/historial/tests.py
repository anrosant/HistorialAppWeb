# Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status, generics
from django.core.urlresolvers import reverse

from django.test import TestCase

from .serializers import UsuarioSerializer
from .models import *
class ModelTestCase(TestCase):
    """Esta clase define el test para el modelos usuario."""
    def setUp(self):
        """las variables."""
        self.usuario_name = "anrosant"
        self.usuario = Usuario(usuario=self.usuario_name)
    def test_crear_usuario(self):
        """Test Usuario model puede crear un Usuario."""
        old_count = Usuario.objects.count()
        self.usuario.save()
        new_count = Usuario.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test para las api views."""
    def setUp(self):
        """Define el test client y otras variables."""
        self.client = APIClient()
        self.usuario_data = {'usuario': 'anrosant'}
        self.response = self.client.post( reverse('create'), self.usuario_data, format="json")
    def test_crear_usuario(self):
        """test para saber si la api tiene la capacidad de crear un usuario."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def test_get_usuario(self):
    """Test the api can get a given bucketlist."""
    usuario = Usuario.objects.get()
    response = self.client.get( reverse('details', kwargs={'pk': usuario.id}), format="json")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, usuario)

def test_update_usuario(self):
    """Test the api can update a given bucketlist."""
    usuario = Usuario.objects.get()
    change_usuario = {'usuario': 'Something new'}
    res = self.client.put( reverse('details', kwargs={'pk': usuario.id}), change_usuario, format='json' )
    self.assertEqual(res.status_code, status.HTTP_200_OK)
def test_delete_usuario(self):
    """Test the api can delete a bucketlist."""
    usuario = Usuario.objects.get()
    response = self.client.delete( reverse('details', kwargs={'pk': usuario.id}), format='json', follow=True)
    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)