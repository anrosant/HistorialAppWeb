from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core import serializers as ser

from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny

from .serializers import *

class CrearEmpleadoView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()

class ListaEmpleadoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class CrearConsultaMedicaView(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaConsultaMedicaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class CrearAtencionEnfermeriaView(generics.ListCreateAPIView):
    queryset = AtencionEnfermeria.objects.all()
    serializer_class = AtencionEnfermeriaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAtencionEnfermeriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AtencionEnfermeria.objects.all()
    serializer_class = AtencionEnfermeriaSerializer

class CrearSignosVitalesView(generics.ListCreateAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaSignosVitalesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer

class CrearEnfermedadView(generics.ListCreateAPIView):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaEnfermedadView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer

class CrearDiagnosticoView(generics.ListCreateAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaDiagnosticoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class CrearPermisoMedicoView(generics.ListCreateAPIView):
    queryset = PermisoMedico.objects.all()
    serializer_class = PermisoMedicoSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaPermisoMedicoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PermisoMedico.objects.all()
    serializer_class = PermisoMedicoSerializer

class CrearInmunizacionView(generics.ListCreateAPIView):
    queryset = Inmunizacion.objects.all()
    serializer_class = InmunizacionSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaInmunizacionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inmunizacion.objects.all()
    serializer_class = InmunizacionSerializer

class CrearVacunaView(generics.ListCreateAPIView):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaVacunaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer

class CrearFichaMedicaView(generics.ListCreateAPIView):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaFichaMedicaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer

class CrearAparatoSistemaView(generics.ListCreateAPIView):
    queryset = AparatoSistema.objects.all()
    serializer_class = AparatoSistemaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAparatoSistemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AparatoSistema.objects.all()
    serializer_class = AparatoSistemaSerializer

class CrearAntecedentePatologicoPersonal(generics.ListCreateAPIView):
    queryset = AntecedentePatologicoPersonal.objects.all()
    serializer_class = AntecedentePatologicoPersonalSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAntecedentePatologicoPersonalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AntecedentePatologicoPersonal.objects.all()
    serializer_class = AntecedentePatologicoPersonalSerializer

class CrearAntecedentePatologicoFamiliarView(generics.ListCreateAPIView):
    queryset = AntecedentePatologicoFamiliar.objects.all()
    serializer_class = AntecedentePatologicoFamiliarSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAntecedentePatologicoFamiliarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AntecedentePatologicoFamiliar.objects.all()
    serializer_class = AntecedentePatologicoFamiliarSerializer

class CrearEmpresaView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaEmpresaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class CrearAntecedenteLaboralView(generics.ListCreateAPIView):
    queryset = AntecedenteLaboral.objects.all()
    serializer_class = AntecedenteLaboralSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaAntecedenteLaboralView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AntecedenteLaboral.objects.all()
    serializer_class = AntecedenteLaboralSerializer

class CrearFactorRiesgoView(generics.ListCreateAPIView):
    queryset = FactorRiesgo.objects.all()
    serializer_class = FactorRiesgoSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaFactorRiesgoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactorRiesgo.objects.all()
    serializer_class = FactorRiesgoSerializer

class CrearExamenLaboratorioView(generics.ListCreateAPIView):
    queryset = ExamenLaboratorio.objects.all()
    serializer_class = ExamenLaboratorioSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaExamenLaboratorioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamenLaboratorio.objects.all()
    serializer_class = ExamenLaboratorioSerializer

class CrearSomaticoGeneralView(generics.ListCreateAPIView):
    queryset = SomaticoGeneral.objects.all()
    serializer_class = SomaticoGeneralSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaSomaticoGeneralView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SomaticoGeneral.objects.all()
    serializer_class = SomaticoGeneralSerializer

class CrearRegionalView(generics.ListCreateAPIView):
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaRegionalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer

class CrearColumnaView(generics.ListCreateAPIView):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaColumnaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer

class CrearRegionLumbarView(generics.ListCreateAPIView):
    queryset = RegionLumbar.objects.all()
    serializer_class = RegionLumbarSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaRegionLumbarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegionLumbar.objects.all()
    serializer_class = RegionLumbarSerializer

class CrearExtremidadesView(generics.ListCreateAPIView):
    queryset = Extremidades.objects.all()
    serializer_class = ExtremidadesSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaExtremidadesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extremidades.objects.all()
    serializer_class = ExtremidadesSerializer

class CrearLocalizacionView(generics.ListCreateAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaLocalizacionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

class CrearExamenFisicoView(generics.ListCreateAPIView):
    queryset = ExamenFisico.objects.all()
    serializer_class = ExamenFisicoSerializer
    def perform_create(self, serializer):
        serializer.save()

class ListaExamenFisicoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamenFisico.objects.all()
    serializer_class = ExamenFisicoSerializer

@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def ingresoUsuario(request):
    context = {}
    if(request.method == 'POST'):
        user = request.data['usuario']
        password = request.data['password']
        try:
            usuario = authenticate(username=user, password=password)
        except User.DoesNotExist:
            usuario = None
        if usuario is not None and not usuario.is_superuser:
            '''Función que genera tokens de usuarios'''
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            usuario = User.objects.get(username=user)
            payload = jwt_payload_handler(usuario)
            token = jwt_encode_handler(payload)
            context["token"] = token
            usuario.token = token
            context["usuarioId"] = usuario.id
            context["empleadoId"] = usuario.profile.empleado.id
            context["msj"] = "Ingreso exitoso"
            dataEmpleado = ser.serialize("json", Empleado.objects.all())
            context["empleado"] = dataEmpleado
            dataEnfermedad = ser.serialize("json", Enfermedad.objects.all())
            context["enfermedad"] = dataEnfermedad
            dataConsultaMedica = ser.serialize("json", ConsultaMedica.objects.all())
            context["consultaMedica"] = dataConsultaMedica
            dataAtencionEnfermeria = ser.serialize("json", AtencionEnfermeria.objects.all())
            context["atencionEnfermeria"] = dataAtencionEnfermeria
            dataDiagnostico = ser.serialize("json", Diagnostico.objects.all())
            context["diagnostico"] = dataDiagnostico
            dataPatologiasPersonales = ser.serialize("json", AntecedentePatologicoPersonal.objects.all())
            context["patologiasPersonales"] = dataPatologiasPersonales
            dataPatologiasFamiliares = ser.serialize("json", AntecedentePatologicoFamiliar.objects.all())
            context["patologiasFamiliares"] = dataPatologiasFamiliares
            dataSignosVitales = ser.serialize("json", SignosVitales.objects.all())
            context["signosVitales"] = dataSignosVitales
            dataPermisoMedico = ser.serialize("json", PermisoMedico.objects.all())
            context["permisoMedico"] = dataPermisoMedico
        else:
            context["msj"]="Usuario o contraseña incorrectos"
    else:
        context["msj"] = "No tiene permisos"
    return Response(context)
