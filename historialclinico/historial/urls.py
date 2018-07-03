from django.conf.urls import url
from . import views
from . import apiView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'historial'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginUser, name='login'),
    url(r'^cerrarSesion/$', views.cerrarSesion, name='cerrarSesion'),
    url(r'^usuario/$', apiView.CrearUsuarioView.as_view(), name="create"),
    url(r'^usuario/(?P<pk>[0-9]+)/$', apiView.ListaUsuarioView.as_view(), name="details"),
    url(r'^empleado/$', apiView.CrearEmpleadoView.as_view(), name="create"),
    url(r'^empleado/(?P<pk>[0-9]+)/$', apiView.ListaEmpleadoView.as_view(), name="details")
]

urlpatterns = format_suffix_patterns(urlpatterns)