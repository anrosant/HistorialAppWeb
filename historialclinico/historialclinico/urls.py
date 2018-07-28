from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('historial.urls')),
    path('api/', include('api.urls'))
]
#path('rest-auth/', include('rest_auth.urls'))