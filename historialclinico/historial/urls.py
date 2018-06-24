from django.conf.urls import url
from . import views

app_name = 'historial'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginUser, name='login'),
    url(r'^cerrarSesion/$', views.cerrarSesion, name='cerrarSesion'),
]
