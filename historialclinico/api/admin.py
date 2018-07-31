from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'get_empleado')
    list_select_related = ('profile', )

    def get_empleado(self, instance):
        return instance.profile.empleado

    get_empleado.short_description = 'Empleado'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Empleado)
admin.site.register(ConsultaMedica)
admin.site.register(AtencionEnfermeria)
admin.site.register(SignosVitales)
admin.site.register(Enfermedad)
admin.site.register(Diagnostico)
admin.site.register(PermisoMedico)
admin.site.register(Inmunizacion)
admin.site.register(Vacuna)
admin.site.register(FichaMedica)
admin.site.register(AparatoSistema)
admin.site.register(AntecedentePatologicoPersonal)
admin.site.register(AntecedentePatologicoFamiliar)
admin.site.register(Empresa)
admin.site.register(AntecedenteLaboral)
admin.site.register(FactorRiesgo)
admin.site.register(ExamenLaboratorio)
admin.site.register(SomaticoGeneral)
admin.site.register(Regional)
admin.site.register(Columna)
admin.site.register(Lumbar)
admin.site.register(Extremidades)
admin.site.register(Localizacion)
admin.site.register(ExamenFisico)