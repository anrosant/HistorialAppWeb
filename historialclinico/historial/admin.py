from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(SignosVitales)
admin.site.register(ConsultaMedica)
admin.site.register(AtencionEnfermeria)