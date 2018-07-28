from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.defaults import page_not_found


''' Esta vista me redirige a la página principal
    Valida si existe el usuario o no'''
def index(request):
    template = loader.get_template('historial/index.html')
    try:
        usuario = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
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
        usuario = authenticate(username=nombre, password=clave)
        if usuario is not None:
            usuario = User.objects.get(username=nombre)
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

'''
def mi_error_404(request):
    nombre_template = 'historial/error404.html'

    return page_not_found(request, template_name=nombre_template)'''