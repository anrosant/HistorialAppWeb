from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from datetime import date
from api.models import *
import time

''' Esta vista me redirige a la página principal
    Valida si existe el usuario o no'''


@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('historial/index.html')
    usuario = User.objects.get(username=request.user.username)
    lista_empleados = Empleado.objects.all()
    context = {
        'usuario': usuario,
        'listaEmpleados': lista_empleados
    }
    return HttpResponse(template.render(context, request))


def loginUser(request):
    template = loader.get_template('historial/login.html')
    if(request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        usuario = authenticate(request, username=nombre, password=clave)
        if usuario is not None:
            login(request, usuario)
            return redirect('historial:index')
        else:
            notice = 'Usuario y/o contraseña incorrectos'
    else:
        notice = 'none'
    context = {
        'notice': notice
    }
    return HttpResponse(template.render(context, request))

def cerrarSesion(request):
    logout(request)
    return redirect('historial:login')


'''
def mi_error_404(request):
    nombre_template = 'historial/error404.html'
    return page_not_found(request, template_name=nombre_template)'''


@login_required(login_url='/login/')
def nuevaFichaMedica(request):
    template = loader.get_template('historial/nueva_ficha_medica.html')
    usuario = User.objects.get(username=request.user.username)
    tipos_riesgos = FactorRiesgo.TIPOS
    nombres_riesgos = FactorRiesgo.NOMBRES
    tipos_ficha = FichaMedica.TIPOS
    lugares = AntecedentePatologicoPersonal.LUGARES
    fecha_ficha = date.today().strftime("%Y-%m-%d")
    nombres_vacunas = Vacuna.NOMBRES
    dosis_vacunas = Vacuna.DOSIS
    nombres_aparatos = AparatoSistema.NOMBRES
    tipos_examenes_laboratorio = ExamenLaboratorio.EXAMENES
    antecedentes = Antecedente.ANTECEDENTES
    alcohol = Habito.ALCOHOL
    tabaco = Habito.TABACO
    id_empleado = '0'
    if (request.method == 'POST'):
        id_empleado = request.POST.get('id_empleado')
    context = {
        'usuario': usuario,
        'tipos': tipos_riesgos,
        'nombres': nombres_riesgos,
        'fecha_ficha': fecha_ficha,
        'tipos_ficha': tipos_ficha,
        'lugares': lugares,
        'nombres_vacunas': nombres_vacunas,
        'dosis_vacunas': dosis_vacunas,
        'nombres_aparatos': nombres_aparatos,
        'tipos_examenes_laboratorio': tipos_examenes_laboratorio,
        'antecedentes': antecedentes,
        'alcohol': alcohol,
        'tabaco': tabaco,
        'id_empleado': id_empleado
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def nuevoEmpleado(request):
    template = loader.get_template('historial/nuevo_empleado.html')
    usuario = User.objects.get(username=request.user.username)
    context = {
        'usuario': usuario
    }
    return HttpResponse(template.render(context, request))

'''
    Permite crear un empleado
    hace post
'''
@login_required(login_url='/login/')
def guardarEmpleado(request):
    if(request.method == 'POST'):
        nuevoEmpleado = Empleado()
        nuevoEmpleado.foto = request.POST.get('ingreso_foto')
        nuevoEmpleado.nombre = request.POST.get('nombres')
        nuevoEmpleado.apellido = request.POST.get('apellidos')
        nuevoEmpleado.cedula = request.POST.get('cedula')
        nuevoEmpleado.sexo  = request.POST.get('sexo')
        nuevoEmpleado.edad = request.POST.get('edad')
        nuevoEmpleado.estadoCivil = request.POST.get('estado_civil')
        nuevoEmpleado.lugarNacimiento = request.POST.get('lugar_nacimiento')
        nuevoEmpleado.fechaNacimiento = request.POST.get('fecha_nacimiento')
        nuevoEmpleado.correo = request.POST.get('correo')
        nuevoEmpleado.direccion = request.POST.get('direccion')
        nuevoEmpleado.instruccion = request.POST.get('instruccion')
        nuevoEmpleado.profesion = request.POST.get('profesion')
        nuevoEmpleado.ocupacion = request.POST.get('ocupacion')
        nuevoEmpleado.fechaRegistro = time.strftime("%Y-%m-%d")
        nuevoEmpleado.ficha_actual = 0
        nuevoEmpleado.save()

        return redirect('historial:index')