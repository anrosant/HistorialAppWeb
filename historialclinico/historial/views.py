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
        'listaEmpleados': lista_empleados,
        'id_empleado': 0
    }
    return HttpResponse(template.render(context, request))


def loginUser(request):
    template = loader.get_template('historial/login.html')
    if(request.method == 'POST'):
        nombre = request.POST['usuario']
        clave = request.POST['password']
        usuario = authenticate(request, username=nombre, password=clave)
        if usuario is not None and not usuario.is_superuser:
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
def nuevaFichaMedica(request, empleado):
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
    #id_empleado = '0'
    tipo_inicial = True
    #empleado = None
    enfermedades = Enfermedad.objects.all()
    #if (request.method == 'GET'):
        #id_empleado = request.GET.get('id_empleado')
    empleado_obj = Empleado.objects.get(id=empleado)
    id_empleado = empleado
    if(empleado_obj.ficha_actual > 0):
        tipo_inicial = False

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
        'empleado': empleado_obj,
        'id_empleado': id_empleado,
        'tipo_inicial': tipo_inicial,
        'enfermedades': enfermedades
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def nuevoEmpleado(request):
    template = loader.get_template('historial/nuevo_empleado.html')
    usuario = User.objects.get(username=request.user.username)
    id_empleado = 0
    if (request.method == 'POST'):
        id_empleado = request.POST.get('id_empleado')
    context = {
        'usuario': usuario,
        'id_empleado': id_empleado
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def infoEmpleado(request):
    template = loader.get_template('historial/info_empleado.html')
    usuario = User.objects.get(username=request.user.username)
    id_empleado = 0
    empleado = usuario.profile.empleado
    if (request.method == 'POST'):
        id_empleado = request.POST.get('id_empleado')
    context = {
        'usuario': usuario,
        'id_empleado': id_empleado,
        'empleado': empleado
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def consultarFicha(request, empleado):
    template = loader.get_template('historial/lista_ficha_medica_empleado.html')
    usuario = User.objects.get(username=request.user.username)
    lista_fichas_empleado = FichaMedica.objects.filter(empleado=empleado)
    empleado_obj = Empleado.objects.get(id=empleado)
    context = {
        'usuario': usuario,
        'lista_fichas_empleado': lista_fichas_empleado,
        'empleado': empleado_obj,
        'id_empleado': empleado
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


'''
    Permite guardar una ficha médica de un empleado
    hace post
'''
@login_required(login_url='/login/')
def guardarFichaMedica(request):
    if(request.method == 'POST'):
        id_empleado = request.POST.get('id_empleado')
        empleado = Empleado.objects.get(pk = id_empleado)

        nueva_ficha = FichaMedica()
        nueva_ficha.empleado = empleado
        nueva_ficha.inmunizacion = guardarInmunizaciones(request)
        nueva_ficha.fecha = time.strftime("%Y-%m-%d")
        nueva_ficha.ciudad = request.POST.get('ciudad_ficha')
        nueva_ficha.tipo = request.POST.get('input_ficha_hidden')
        nueva_ficha.prescripcion = request.POST.get('prescripciones_medicas')
        nueva_ficha.save()
        empleado.ficha_actual = nueva_ficha.id
        empleado.save()

        empresa_actual = Empresa()
        empresa_actual.nombre = request.POST.get('nombre_empresa_actual')
        empresa_actual.cargo = request.POST.get('cargo_actual')
        empresa_actual.riesgos = request.POST.get('riesgos')
        empresa_actual.epps = request.POST.get('epps')
        empresa_actual.area_trabajo = request.POST.get('area_trabajo')
        empresa_actual.save()

        antecedente_laboral = AntecedenteLaboral()
        antecedente_laboral.ficha_medica = nueva_ficha
        antecedente_laboral.empresa = empresa_actual
        #antecedente_laboral.tiempo = None
        antecedente_laboral.edad_inicio = request.POST.get('edad_inicio')
        antecedente_laboral.actividades_extralaborales = request.POST.get('actividades_extralaborales')
        antecedente_laboral.actual = True
        antecedente_laboral.save()

        guardarEmpresasAnteriores(request, nueva_ficha)
        guardarAntecedentesPatologicosPersonales(request, nueva_ficha)

        planificacion = request.POST.get('planificacion_familiar')
        if(planificacion in request.POST):
            antecedente_gineco = AntecedenteGinecoObstetrico()
            antecedente_gineco.ficha = nueva_ficha
            antecedente_gineco.fecha_ultima_menstruacion = request.POST.get('fecha_ultima_menstruacion')
            antecedente_gineco.planificacion_familiar = request.POST.get('planificacion_familiar')
            antecedente_gineco.save()

            lista_gineco = request.POST.getlist('antecedente_gineco-obstetrico')
            for x in lista_gineco:
                antecedente = Antecedente()
                antecedente.antecedente_gineco_obstetrico = antecedente_gineco
                antecedente.antecedente = x
                antecedente.save()

        habito = Habito()
        habito.ficha = nueva_ficha
        habito.alcohol = request.POST.get('alcohol')
        habito.tabaco = request.POST.get('tabaco')
        if(request.POST.get('cantidad_tabaco') == ""):
            habito.cantidad_tabaco = None
        else:
            habito.cantidad_tabaco = request.POST.get('cantidad_tabaco')
        habito.save()

        guardarAntecedentesPatologicosFamiliares(request, nueva_ficha)
        guardarAparatoSistema(request, nueva_ficha)

        signos_vitales = SignosVitales()
        signos_vitales.empleado = empleado
        if (request.POST.get('presion_sistolica') == ""):
            signos_vitales.presion_sistolica = None
        else:
            signos_vitales.presion_sistolica = request.POST.get('presion_sistolica')

        if (request.POST.get('presion_distolica') == ""):
            signos_vitales.presion_distolica = None
        else:
            signos_vitales.presion_distolica = request.POST.get('presion_distolica')

        if (request.POST.get('frecuencia_cardiaca') == ""):
            signos_vitales.pulso = None
        else:
            signos_vitales.pulso = request.POST.get('frecuencia_cardiaca')

        if (request.POST.get('temperatura') == ""):
            signos_vitales.temperatura = None
        else:
            signos_vitales.temperatura = request.POST.get('temperatura')
        signos_vitales.save()

        somatico = SomaticoGeneral()
        somatico.apariencia = request.POST.get('apariencia')
        somatico.estado_nutricional = request.POST.get('estado_nutricional')
        somatico.actividades_psicomotoras = request.POST.get('actividades_psicomotoras')
        somatico.save()

        columna = guardarColumna(request)
        region_lumbar = guardarRegionLumbar(request)
        extremidades = guardarExtremidades(request)

        regional = Regional()
        regional.piel_tegumentos = request.POST.get('piel_tegumentos')
        regional.cabeza_cuello = request.POST.get('cabeza_cuello')
        regional.torax = request.POST.get('torax')
        regional.corazon = request.POST.get('corazon')
        regional.pulmones = request.POST.get('pulmones')
        regional.abdomen = request.POST.get('abdomen')
        regional.save()

        examen_fisico = ExamenFisico()
        examen_fisico.ficha_medica = nueva_ficha
        examen_fisico.signos_vitales = signos_vitales
        examen_fisico.somatico_general = somatico
        examen_fisico.columna = columna
        examen_fisico.region_lumbar = region_lumbar
        examen_fisico.extremidades = extremidades
        examen_fisico.regional = regional

        if (request.POST.get('talla') == ""):
            examen_fisico.talla = None
        else:
            examen_fisico.talla = request.POST.get('talla')

        if (request.POST.get('peso') == ""):
            examen_fisico.peso = None
        else:
            examen_fisico.peso = request.POST.get('peso')

        if (request.POST.get('indice_masa_corporal') == ""):
            examen_fisico.indice_masa_corporal = None
        else:
            examen_fisico.indice_masa_corporal = request.POST.get('indice_masa_corporal')

        if(request.POST.get('frecuencia_respiratoria') == ""):
            examen_fisico.frecuencia_respiratoria = None
        else:
            examen_fisico.frecuencia_respiratoria = request.POST.get('frecuencia_respiratoria')

        examen_fisico.examen_neurologico_elemental = request.POST.get('examen_neurologico_elemental')
        examen_fisico.save()

        guardarExamenesLaboratorio(request, nueva_ficha)
        guardarDiagnosticos(request, nueva_ficha)

        vulnerabilidad = Vulnerabilidad()
        vulnerabilidad.ficha_medica = nueva_ficha

        if (request.POST.get('persona_vulnerable') == 'Sí'):
            vulnerabilidad.persona_vulnerable = True
        elif (request.POST.get('persona_vulnerable') == 'No'):
            vulnerabilidad.persona_vulnerable = False

        if (request.POST.get('persona_discapacidad') == 'Sí'):
            vulnerabilidad.persona_discapacidad = True
        elif (request.POST.get('persona_discapacidad') == 'No'):
            vulnerabilidad.persona_discapacidad = False

        vulnerabilidad.descripcion = request.POST.get('descripcion_vulnerabilidad')
        vulnerabilidad.save()

        return redirect('historial:consultarFicha', id_empleado)

def guardarInmunizaciones(request):
    lista = ['tetanos', 'hepatitis', 'tifoidea', 'amarilla']
    observacion = request.POST.get('observacion_vacuna')
    inmunizacion = Inmunizacion()
    inmunizacion.observacion = observacion
    inmunizacion.save()
    for va in lista:
        i = 1
        dosis = request.POST.get('dosis_vacuna_' + va + '_' + str(i))
        fecha = request.POST.get('fecha_vacuna_' + va + '_' + str(i))
        while dosis in request.POST and fecha in request.POST:
            if(dosis == "Escoja una opción"):
                break
            nueva_vacuna = Vacuna()
            if(va == 'tetanos'):
                nueva_vacuna.nombre = 'Tétanos'
            elif(va == 'hepatitis'):
                nueva_vacuna.nombre = 'Hepatitis A - B'
            elif (va == 'tifoidea'):
                nueva_vacuna.nombre = 'Fiebre tifoidea'
            elif (va == 'amarilla'):
                nueva_vacuna.nombre = 'Fiebre amarilla'
            nueva_vacuna.dosis = dosis
            nueva_vacuna.fecha = fecha
            nueva_vacuna.inmunizacion = inmunizacion
            nueva_vacuna.save()
            i = i + 1
            dosis = request.POST.get('dosis_vacuna_' + va + '_' + str(i))
            fecha = request.POST.get('fecha_vacuna_' + va + '_' + str(i))
    return inmunizacion

def guardarEmpresasAnteriores(request, nueva_ficha):
    i = 1
    nombre_empresa_anterior = request.POST.get('nombre_empresa_anterior_' + str(i))
    while nombre_empresa_anterior in request.POST:
        if(nombre_empresa_anterior == ''):
            break
        empresa_anterior = Empresa()
        empresa_anterior.nombre = nombre_empresa_anterior
        empresa_anterior.cargo = request.POST.get('cargo_empresa_anterior_' + str(i))
        empresa_anterior.save()
        j = 1
        tipo_riesgo_anterior = request.POST.get('tipo_riesgo_anterior_' + str(i) + '_' + str(j))
        while tipo_riesgo_anterior in request.POST:
            if (tipo_riesgo_anterior == "Escoja una opción"):
                break
            factor_riesgo = FactorRiesgo()
            factor_riesgo.empresa = empresa_anterior
            factor_riesgo.tipo = tipo_riesgo_anterior
            factor_riesgo.nombre = request.POST.get('nombre_riesgo_anterior_' + str(i) + '_' + str(j))
            factor_riesgo.save()
            j = j + 1
            tipo_riesgo_anterior = request.POST.get('tipo_riesgo_anterior_' + str(i) + '_' + str(j))
        antecedente_empresa_anterior = AntecedenteLaboral()
        antecedente_empresa_anterior.ficha_medica = nueva_ficha
        antecedente_empresa_anterior.empresa = empresa_anterior
        antecedente_empresa_anterior.tiempo = request.POST.get('tiempo_empresa_anterior_' + str(i))
        antecedente_empresa_anterior.actual = False
        antecedente_empresa_anterior.save()
        i = i + 1
        nombre_empresa_anterior = request.POST.get('nombre_empresa_anterior_' + str(i))
    return

def guardarAntecedentesPatologicosPersonales(request, nueva_ficha):
    i = 1
    lugar = request.POST.get('lugar_patologia_personal_' + str(i))
    while lugar in request.POST:
        if(lugar == "Escoja una opción"):
            break
        antecedente_personal = AntecedentePatologicoPersonal()
        antecedente_personal.ficha = nueva_ficha
        antecedente_personal.lugar = lugar
        antecedente_personal.detalle = request.POST.get('detalle_patologia_personal_' + str(i))
        antecedente_personal.save()
        i = i + 1
        lugar = request.POST.get('lugar_patologia_personal_' + str(i))

def guardarAntecedentesPatologicosFamiliares(request, nueva_ficha):
    i = 1
    parentesco = request.POST.get('parentesco_patologia_familiar_' + str(i))
    while parentesco in request.POST:
        if (parentesco == ""):
            break
        antecedente_familiar = AntecedentePatologicoFamiliar()
        antecedente_familiar.ficha = nueva_ficha
        antecedente_familiar.parentesco = parentesco
        antecedente_familiar.patologia = request.POST.get('nombre_patologia_familiar_' + str(i))
        antecedente_familiar.detalle = request.POST.get('detalle_patologia_familiar_' + str(i))
        antecedente_familiar.save()
        i = i + 1
        parentesco = request.POST.get('parentesco_patologia_familiar_' + str(i))

def guardarAparatoSistema(request, nueva_ficha):
    i = 1
    nombre = request.POST.get('nombre_aparato_sistema_' + str(i))
    while nombre in request.POST:
        if (nombre == "Escoja una opción"):
            break
        aparato = AparatoSistema()
        aparato.ficha_medica = nueva_ficha
        aparato.nombre = nombre
        aparato.detalle = request.POST.get('detalle_aparato_sistema_' + str(i))
        aparato.save()
        i = i + 1
        nombre = request.POST.get('nombre_aparato_sistema_' + str(i))

def guardarColumna(request):
    columna = Columna()

    if(request.POST.get('cifosis_acentuada') == 'Sí'):
        columna.cifosis_acentuada = True
    elif(request.POST.get('cifosis_acentuada') == 'No'):
        columna.cifosis_acentuada = False

    if(request.POST.get('contractura_muscular') == 'Sí'):
        columna.contractura_muscular = True
    elif(request.POST.get('contractura_muscular') == 'No'):
        columna.contractura_muscular = False

    if (request.POST.get('dolor_columna') == 'Sí'):
        columna.dolor = True
    elif(request.POST.get('dolor_columna') == 'No'):
        columna.dolor = False

    if (request.POST.get('lordosis_acentuada') == 'Sí'):
        columna.lordosis_acentuada = True
    elif(request.POST.get('lordosis_acentuada') == 'No'):
        columna.lordosis_acentuada = False

    if(request.POST.get('escoliosis') == 'Sí'):
        columna.escoliosis = True
    elif(request.POST.get('escoliosis') == 'No'):
        columna.escoliosis = False

    columna.motricidad = request.POST.get('motricidad_columna')
    columna.detalle_alteracion = request.POST.get('detalle_alteracion_columna')
    columna.save()

    lugares = request.POST.get('lassegue')
    if(lugares != None):
        for l in lugares:
            localizacion = Localizacion()
            localizacion.columna = columna
            localizacion.tipo = 'lassegue'
            localizacion.lugar = l
            localizacion.save()

    return columna

def guardarRegionLumbar(request):
    region_lumbar = RegionLumbar()

    if(request.POST.get('dolor_punio_percusion') == 'Sí'):
        region_lumbar.dolor_punio_percusion = True
    elif(request.POST.get('dolor_punio_percusion') == 'No'):
        region_lumbar.dolor_punio_percusion = False

    region_lumbar.motricidad = request.POST.get('motricidad_lumbar')
    region_lumbar.detalle_alteracion = request.POST.get('detalle_alteracion_lumbar')
    region_lumbar.save()

    return region_lumbar

def guardarExtremidades(request):
    extremidades = Extremidades()

    if(request.POST.get('dolor_extremidades') == 'Sí'):
        extremidades.dolor = True
    elif(request.POST.get('dolor_extremidades') == 'No'):
        extremidades.dolor = False

    extremidades.motricidad = request.POST.get('motricidad_extremidades')
    extremidades.observaciones = request.POST.get('detalle_alteracion_extremidades')
    extremidades.save()

    lista = ['phalen', 'tinel', 'signo_cajon', 'finkelstein']
    for a in lista:
        lugares = request.POST.getlist(a)
        if (lugares != None):
            for l in lugares:
                localizacion = Localizacion()
                localizacion.extremidades = extremidades
                localizacion.tipo = a
                localizacion.lugar = l
                localizacion.save()

    return extremidades

def guardarExamenesLaboratorio(request, nueva_ficha):
    i = 1
    hallazgos = request.POST.get('hallazgos_examen_laboratorio_' + str(i))
    while hallazgos in request.POST:
        if (hallazgos == ""):
            break
        examen_laboratorio = ExamenLaboratorio()
        examen_laboratorio.ficha_medica = nueva_ficha
        examen_laboratorio.tipo = request.POST.get('tipo_examen_laboratorio_' + str(i))
        examen_laboratorio.descripcion = request.POST.get('hallazgos_examen_laboratorio_' + str(i))
        examen_laboratorio.imagen = request.POST.get('ingreso_examen_' + str(i))
        examen_laboratorio.save()
        i = i + 1
        hallazgos = request.POST.get('hallazgos_examen_laboratorio_' + str(i))

def guardarDiagnosticos(request, nueva_ficha):
    i = 1
    enfer = request.POST.get('enfermedad_' + str(i))
    while enfer in request.POST:
        if (enfer == "Escoja una opción"):
            break
        enfermedad = Enfermedad.objects.filter(codigo=enfer)
        # enfermedad = Enfermedad()
        # enfermedad.grupo = "Enfermedades infecciosas intestinales"
        # enfermedad.nombre = enfermedad[6:]
        # enfermedad.codigo = enfermedad[0:2]
        # enfermedad.save()

        diagnostico = Diagnostico()
        diagnostico.enfermedad = enfermedad
        diagnostico.ficha_medica = nueva_ficha
        diagnostico.tipoEnfermedad = request.POST.get('tipo_diagnostico_' + str(i))
        diagnostico.save()
        i = i + 1
        enfermedad = request.POST.get('enfermedad_' + str(i))