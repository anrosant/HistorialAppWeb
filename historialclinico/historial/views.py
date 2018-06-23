from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from historial.models import Usuario

''' Esta vista me redirge a la página principal
    Valida si existe el usuario o no'''
def index(request):
    template = loader.get_template('historial/index.html')
    try:
        usuario = Usuario.objects.get(usuario=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None
    if usuario is not None:
        usuario = usuario
    else:
        return redirect('historial:login')
    context = {
        'usuario': usuario
    }
    return HttpResponse(template.render(context, request))

def loginUser(request):
    template = loader.get_template('historial/login.html')
    if (request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        try:
            usuario = Usuario.objects.get(usuario=nombre, contrasenia=clave)
        except Usuario.DoesNotExist:
            usuario = None
        if usuario is not None:
            template = loader.get_template('historial/index.html')
            context = {
                'usuario': usuario,
            }
            return HttpResponse(template.render(context, request))
        else:
            notice = 'Ingreso Invalido'
    else:
        notice = 'none'
    context = {
        'notice': notice
    }
    return HttpResponse(template.render(context, request))
def cerrarSesion(request):
    logout(request)
    return redirect('historial:login')