from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'historial'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginUser, name='login'),
    url(r'^cerrarSesion/$', views.cerrarSesion, name='cerrarSesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
'''url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),'''