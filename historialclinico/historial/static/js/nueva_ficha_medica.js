$(document).ready(function() {
    $("#talla").keypress(function (e) {
        return !!($.isNumeric(e.key) || e.key === "." || e.key === ",");
    });
    $("#peso").keypress(function (e) {
        return !!($.isNumeric(e.key) || e.key === "." || e.key === ",");
    });
    $("#presion_sistolica").keypress(function (e) {
        return !!($.isNumeric(e.key));
    });
    $("#presion_distolica").keypress(function (e) {
        return !!($.isNumeric(e.key));
    });
    $("#frecuencia_cardiaca").keypress(function (e) {
        return !!($.isNumeric(e.key));
    });
    $("#frecuencia_respiratoria").keypress(function (e) {
        return !!($.isNumeric(e.key));
    });
    $("#temperatura").keypress(function (e) {
        return !!($.isNumeric(e.key) || e.key === "." || e.key === ",");
    });
});

function escogerTipo(tipo, empresa, riesgo) {
    var tipo_r;
    var nombre;
    var opciones;
    var i;
    if(tipo === 'anterior') {
        tipo_r = $("#tipo_riesgo_" + tipo + "_" + empresa + "_" + riesgo).val();
        nombre = $("#nombre_riesgo_" + tipo + "_" + empresa + "_" + riesgo);
        opciones = $("#nombre_riesgo_" + tipo + "_" +  empresa + "_" + riesgo + " option");
        for (i = 1; i < opciones.length; i++) {
            if ($(opciones[i]).attr("class") !== tipo_r) {
                $(opciones[i]).attr("hidden", "");
            } else {
                $(opciones[i]).removeAttr("hidden");
            }
        }
    } else {
        tipo_r = $("#tipo_riesgo_" + tipo + "_" + riesgo).val();
        nombre = $("#nombre_riesgo_" + tipo + "_" + riesgo);
        opciones = $("#nombre_riesgo_" + tipo + "_" + riesgo + " option");
        for (i = 1; i < opciones.length; i++) {
            if ($(opciones[i]).attr("class") !== tipo_r) {
                $(opciones[i]).attr("hidden", "");
            } else {
                $(opciones[i]).removeAttr("hidden");
            }
        }
    }
}

function agregarRiesgo() {
    var containers_tipo_riesgo = $(".container_tipo_riesgo_actual");
    var containers_nombre_riesgo = $(".container_nombre_riesgo_actual");
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_actual");
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_tipo_riesgo[0]).clone(false, true).appendTo("#container_riesgos_actuales");
    $(containers_nombre_riesgo[0]).clone(false, true).appendTo("#container_riesgos_actuales");
    restablecerCopia("#container_riesgos_actuales");
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_riesgos_actuales");
    $("#boton_mas_riesgo_empresa_actual").appendTo("#container_riesgos_actuales");
    ordenarRiesgo();
}

function restablecerCopia(elemento){
    var cont = $(elemento).children();
    var select = $(cont[cont.length - 1]).children()[0];
    var opci = $(select).children();
    for(var i = 0; i < opci.length; i++) {
        var attr1 = $(opci[i]).attr("hidden");
        var attr2 = $(opci[i]).attr("disabled");
        if((typeof attr1 !== typeof undefined || attr1 !== false) &&
            (typeof attr2 === typeof undefined || attr2 === false)) {
            $(opci[i]).removeAttr("hidden");
        }
    }
}

function eliminarRiesgo(numero) {
    $("#tipo_riesgo_actual_" + numero).parent().remove();
    $("#nombre_riesgo_actual_" + numero).parent().remove();
    $("#boton_eliminar_riesgo_actual_" + numero).parent().remove();
    var containers_tipo_riesgo = $(".container_tipo_riesgo_actual");
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_actual");
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarRiesgo();
}

function ordenarRiesgo() {
    var containers_tipo_riesgo = $(".container_tipo_riesgo_actual");
    var containers_nombre_riesgo = $(".container_nombre_riesgo_actual");
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_actual");
    for(var i = 0; i < containers_tipo_riesgo.length; i++) {
        $($(containers_tipo_riesgo[i]).children()[0]).attr('id', 'tipo_riesgo_actual_' + (i + 1));
        $($(containers_tipo_riesgo[i]).children()[0]).attr('name', 'tipo_riesgo_actual_' + (i + 1));
        $($(containers_tipo_riesgo[i]).children()[0]).attr('onchange', 'escogerTipo("actual", 0, ' + (i + 1) + ')');
        $($(containers_nombre_riesgo[i]).children()[0]).attr('id', 'nombre_riesgo_actual_' + (i + 1));
        $($(containers_nombre_riesgo[i]).children()[0]).attr('name', 'nombre_riesgo_actual_' + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('onclick', 'eliminarRiesgo("actual", ' + (i + 1) + ')');
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_riesgo_actual_' + (i + 1));
    }
}

function agregarRiesgoAnterior(empresa) {
    var containers_tipo_riesgo = $(".container_tipo_riesgo_anterior_" + empresa);
    var containers_nombre_riesgo = $(".container_nombre_riesgo_anterior_" + empresa);
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_anterior_" + empresa);
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_tipo_riesgo[0]).clone(false, true).appendTo("#container_riesgo_anterior_" + empresa);
    $(containers_nombre_riesgo[0]).clone(false, true).appendTo("#container_riesgo_anterior_" + empresa);
    restablecerCopia(".container_riesgos_anteriores");
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_riesgo_anterior_" + empresa);
    $("#boton_mas_riesgo_empresa_anterior_" + empresa).appendTo("#container_riesgo_anterior_" + empresa);
    ordenarRiesgoAnterior();
}

function eliminarRiesgoAnterior(empresa, riesgo) {
    $("#tipo_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
    $("#nombre_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
    $("#boton_eliminar_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
    var containers_tipo_riesgo = $(".container_tipo_riesgo_anterior_" + empresa);
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_anterior_" + empresa);
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarRiesgoAnterior();
}

function ordenarRiesgoAnterior() {
    var containers = $(".container_riesgos_anteriores");
    for(var h = 0; h < containers.length; h++) {
        $(containers[h]).attr('id', 'container_riesgo_anterior_' + (h + 1));
    }
    for(var i = 0; i < containers.length; i++) {
        var containers_tipo_riesgo = $("#container_riesgo_anterior_" + (i + 1) + " [class*='container_tipo_riesgo_anterior_']");
        for(var j = 0; j < containers_tipo_riesgo.length; j++) {
            $(containers_tipo_riesgo[j]).attr('class', 'col-xl-5 col-lg-5 col-md-5 col-sm-5 container_tipo_riesgo_anterior_' + (i + 1));
            $($(containers_tipo_riesgo[j]).children()[0]).attr('id', 'tipo_riesgo_anterior_' + (i + 1) + "_" + (j + 1));
            $($(containers_tipo_riesgo[j]).children()[0]).attr('name', 'tipo_riesgo_anterior_' + (i + 1) + "_" + (j + 1));
            $($(containers_tipo_riesgo[j]).children()[0]).attr('onchange', 'escogerTipo("anterior", ' + (i + 1) + ', ' + (j + 1) + ')');
        }
        var containers_nombre_riesgo = $("#container_riesgo_anterior_" + (i + 1) + " [class*='container_nombre_riesgo_anterior_']");
        for(var k = 0; k < containers_nombre_riesgo.length; k++) {
            $(containers_nombre_riesgo[k]).attr('class', 'col-xl-5 col-lg-5 col-md-5 col-sm-5 container_nombre_riesgo_anterior_' + (i + 1));
            $($(containers_nombre_riesgo[k]).children()[0]).attr('id', 'nombre_riesgo_anterior_' + (i + 1) + "_" + (k + 1));
            $($(containers_nombre_riesgo[k]).children()[0]).attr('name', 'nombre_riesgo_anterior_' + (i + 1) + "_" + (k + 1));
        }
        var botones_eliminar = $("#container_riesgo_anterior_" + (i + 1) + " [class*='boton_eliminar_riesgo_empresa_anterior_']");
        for(var l = 0; l < botones_eliminar.length; l++) {
            $(botones_eliminar[l]).attr('class', 'col-xl-1 col-lg-1 col-md-1 col-sm-1 boton_eliminar_riesgo_empresa_anterior_' + (i + 1));
            $($(botones_eliminar[l]).children()[0]).attr('id', 'boton_eliminar_riesgo_anterior_' + (i + 1) + "_" + (l + 1));
            $($(botones_eliminar[l]).children()[0]).attr('onclick', 'eliminarRiesgoAnterior(' + (i + 1) + ', ' + (l + 1) + ')');
        }
    }
    var botones_mas = $("[id*='boton_mas_riesgo_empresa_anterior_']");
    for(var m = 0; m < botones_mas.length; m++) {
        $(botones_mas[m]).attr('id', 'boton_mas_riesgo_empresa_anterior_' + (m + 1));
        $($(botones_mas[m]).children()[0]).attr('onclick', 'agregarRiesgoAnterior(' + (m + 1) + ')');
    }
}

function agregarEmpresa() {
    var containers_empresas_anteriores = $(".container_empresa_anterior");
    var botones_eliminar = $(".boton_eliminar_empresa_anterior");
    if(containers_empresas_anteriores.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_empresas_anteriores[0]).clone(false, false).appendTo("#container_empresas_anteriores");
    /*var containers_empresas = $("#container_empresas_anteriores");
    var ultima_empresa = $(containers_empresas).children()[$(containers_empresas).children().length - 1];
    var riesgos = $(ultima_empresa).find(".container_riesgos_anteriores select").length / 2;
    console.log("riesgos: "+ riesgos);
    console.log(ultima_empresa);
    //while(riesgos > 1) {
        var empresa = $(".container_empresa_anterior").length;
        var riesgo = riesgos;
        console.log("numero empresas" + empresa);
        console.log("riesgo" + riesgo);
        $("#tipo_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
        console.log($("#tipo_riesgo_anterior_" + empresa + "_" + riesgo));
        $("#nombre_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
        $("#boton_eliminar_riesgo_anterior_" + empresa + "_" + riesgo).parent().remove();
        var containers_tipo_riesgo = $(".container_tipo_riesgo_anterior_" + empresa);
        botones_eliminar = $(".boton_eliminar_riesgo_empresa_anterior_" + empresa);
        if(containers_tipo_riesgo.length === 1) {
            $(botones_eliminar[0]).attr("hidden", "");
        }
        containers_empresas = $("#container_empresas_anteriores");
        ultima_empresa = $(containers_empresas).children()[$(containers_empresas).children().length - 1];
        riesgos = $(ultima_empresa).find(".container_riesgos_anteriores select").length / 2;
        console.log("riesgos: "+ riesgos);
    console.log(ultima_empresa);
    //}*/
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_empresas_anteriores");
    $("#boton_mas_empresa_anterior").appendTo("#container_empresas_anteriores");
    ordenarEmpresa();
}

function eliminarEmpresa(numero) {
    $("#container_empresa_anterior_" + numero).remove();
    $("#boton_eliminar_empresa_anterior_" + numero).parent().remove();
    var containers_empresas_anteriores = $(".container_empresa_anterior");
    var botones_eliminar = $(".boton_eliminar_empresa_anterior");
    if(containers_empresas_anteriores.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarEmpresa();
}

function ordenarEmpresa() {
    var containers_empresas_anteriores = $(".container_empresa_anterior");
    var containers_nombre_empresas_anteriores = $(".container_nombre_empresa_anterior");
    var containers_tiempo_empresas_anteriores = $(".container_tiempo_empresa_anterior");
    var containers_cargo_empresas_anteriores = $(".container_cargo_empresa_anterior");
    var botones_eliminar = $(".boton_eliminar_empresa_anterior");
    for(var i = 0; i < containers_empresas_anteriores.length; i++) {
        $($(containers_empresas_anteriores[i])).attr('id', 'container_empresa_anterior_' + (i + 1));
        $($(containers_nombre_empresas_anteriores[i]).children()[1]).attr('id', 'nombre_empresa_anterior_' + (i + 1));
        $($(containers_tiempo_empresas_anteriores[i]).children()[1]).attr('id', 'tiempo_empresa_anterior_' + (i + 1));
        $($(containers_cargo_empresas_anteriores[i]).children()[1]).attr('id', 'cargo_empresa_anterior_' + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('onclick', 'eliminarEmpresa(' + (i + 1) + ')');
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_empresa_anterior_' + (i + 1));
    }
    ordenarRiesgoAnterior();
}

function agregarPatologia(tipo) {
    var containers_nombre_patologia = $(".container_nombre_patologia_" + tipo);
    var containers_detalle_patologia = $(".container_detalle_patologia_" + tipo);
    var botones_eliminar = $(".boton_eliminar_patologia_" + tipo);
    if(containers_nombre_patologia.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    if(tipo === 'familiar') {
        var containers_parentesco_patologia = $(".container_parentesco_patologia_" + tipo);
        $(containers_parentesco_patologia[0]).clone(false, false).appendTo("#container_patologias_" + tipo + "es");
    }
    $(containers_nombre_patologia[0]).clone(false, false).appendTo("#container_patologias_" + tipo + "es");
    $(containers_detalle_patologia[0]).clone(false, false).appendTo("#container_patologias_" + tipo + "es");
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_patologias_" + tipo + "es");
    $("#boton_mas_patologia_" + tipo).appendTo("#container_patologias_" + tipo + "es");
    ordenarPatologia(tipo);
}

function eliminarPatologia(tipo, numero) {
    if(tipo === 'familiar') {
        $("#parentesco_patologia_" + tipo + "_" + numero).parent().remove();
    }
    $("#nombre_patologia_" + tipo + "_" + numero).parent().remove();
    $("#detalle_patologia_" + tipo + "_" + numero).parent().remove();
    $("#boton_eliminar_patologia_" + tipo + "_" + numero).parent().remove();
    var containers_nombre_patologia = $(".container_nombre_patologia_" + tipo);
    var botones_eliminar = $(".boton_eliminar_patologia_" + tipo);
    if(containers_nombre_patologia.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarPatologia(tipo);
}

function ordenarPatologia(tipo) {
    if(tipo === 'familiar') {
        var containers_parentesco_patologia = $(".container_parentesco_patologia_" + tipo);
    }
    var containers_nombre_patologia = $(".container_nombre_patologia_" + tipo);
    var containers_detalle_patologia = $(".container_detalle_patologia_" + tipo);
    var botones_eliminar = $(".boton_eliminar_patologia_" + tipo);
    for(var i = 0; i < containers_nombre_patologia.length; i++) {
        if(tipo === 'familiar') {
            $($(containers_parentesco_patologia[i]).children()[0]).attr('id', 'parentesco_patologia_' + tipo + "_" + (i + 1));
            $($(containers_parentesco_patologia[i]).children()[0]).attr('name', 'parentesco_patologia_' + tipo + "_" + (i + 1));
        }
        $($(containers_nombre_patologia[i]).children()[0]).attr('id', 'nombre_patologia_' + tipo + "_" + (i + 1));
        $($(containers_nombre_patologia[i]).children()[0]).attr('name', 'nombre_patologia_' + tipo + "_" + (i + 1));
        $($(containers_detalle_patologia[i]).children()[0]).attr('id', 'detalle_patologia_' + tipo + "_" + (i + 1));
        $($(containers_detalle_patologia[i]).children()[0]).attr('name', 'detalle_patologia_' + tipo + "_" + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('onclick', 'eliminarPatologia(\'' + tipo + '\', ' + (i + 1) + ')');
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_patologia_' + tipo + "_" + (i + 1));
    }
}

function agregarVacuna(tipo) {
    var containers_dosis_vacuna = $(".container_dosis_vacuna_" + tipo);
    var containers_fecha_vacuna = $(".container_fecha_vacuna_" + tipo);
    var botones_eliminar = $(".boton_eliminar_vacuna_" + tipo);
    if(containers_dosis_vacuna.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_dosis_vacuna[0]).clone(false, false).appendTo("#inmunizaciones_" + tipo);
    $(containers_fecha_vacuna[0]).clone(false, false).appendTo("#inmunizaciones_" + tipo);
    $(botones_eliminar[0]).clone(false, true).appendTo("#inmunizaciones_" + tipo);
    $("#boton_mas_vacuna_" + tipo).appendTo("#inmunizaciones_" + tipo);
    ordenarVacuna(tipo);
}

function eliminarVacuna(tipo, numero) {
    $("#dosis_vacuna_" + tipo + "_" + numero).parent().remove();
    $("#fecha_vacuna_" + tipo + "_" + numero).parent().remove();
    $("#boton_eliminar_vacuna_" + tipo + "_" + numero).parent().remove();
    var containers_dosis_vacuna = $(".container_dosis_vacuna_" + tipo);
    var botones_eliminar = $(".boton_eliminar_vacuna_" + tipo);
    if(containers_dosis_vacuna.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarVacuna(tipo);
}

function ordenarVacuna(tipo) {
    var containers_dosis_vacuna = $(".container_dosis_vacuna_" + tipo);
    var containers_fecha_vacuna = $(".container_fecha_vacuna_" + tipo);
    var botones_eliminar = $(".boton_eliminar_vacuna_" + tipo);
    for(var i = 0; i < containers_dosis_vacuna.length; i++) {
        $($(containers_dosis_vacuna[i]).children()[0]).attr('id', 'dosis_vacuna_' + tipo + "_" + (i + 1));
        $($(containers_dosis_vacuna[i]).children()[0]).attr('name', 'dosis_vacuna_' + tipo + "_" + (i + 1));
        $($(containers_fecha_vacuna[i]).children()[0]).attr('id', 'fecha_vacuna_' + tipo + "_" + (i + 1));
        $($(containers_fecha_vacuna[i]).children()[0]).attr('name', 'fecha_vacuna_' + tipo + "_" + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('onclick', 'eliminarVacuna(\'' + tipo + '\', ' + (i + 1) + ')');
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_vacuna_' + tipo + "_" + (i + 1));
    }
}

function agregarAparato() {
    var containers_nombre_aparato = $(".container_nombre_aparato_sistema");
    var containers_detalle_aparato = $(".container_detalle_aparato_sistema");
    var botones_eliminar = $(".boton_eliminar_aparato_sistema");
    if(containers_nombre_aparato.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_nombre_aparato[0]).clone(false, false).appendTo("#container_aparatos_sistema");
    $(containers_detalle_aparato[0]).clone(false, false).appendTo("#container_aparatos_sistema");
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_aparatos_sistema");
    $("#boton_mas_aparato_sistema").appendTo("#container_aparatos_sistema");
    ordenarAparato();
}

function eliminarAparato(numero) {
    $("#nombre_aparato_sistema_" + numero).parent().remove();
    $("#detalle_aparato_sistema_" + numero).parent().remove();
    $("#boton_eliminar_aparato_sistema_" + numero).parent().remove();
    var containers_nombre_aparato = $(".container_nombre_aparato_sistema");
    var botones_eliminar = $(".boton_eliminar_aparato_sistema");
    if(containers_nombre_aparato.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarAparato();
}

function ordenarAparato() {
    var containers_nombre_aparato = $(".container_nombre_aparato_sistema");
    var containers_detalle_aparato = $(".container_detalle_aparato_sistema");
    var botones_eliminar = $(".boton_eliminar_aparato_sistema");
    for(var i = 0; i < containers_nombre_aparato.length; i++) {
        $($(containers_nombre_aparato[i]).children()[0]).attr('id', 'nombre_aparato_sistema_' + (i + 1));
        $($(containers_nombre_aparato[i]).children()[0]).attr('name', 'nombre_aparato_sistema_' + (i + 1));
        $($(containers_detalle_aparato[i]).children()[0]).attr('id', 'detalle_aparato_sistema_' + (i + 1));
        $($(containers_detalle_aparato[i]).children()[0]).attr('name', 'detalle_aparato_sistema_' + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_aparato_sistema_' + (i + 1));
    }
}

function calcularIMC() {
    var talla = parseFloat($("#talla").val() / 100);
    var peso = parseFloat($("#peso").val());
    if(!isNaN(talla) && !isNaN(peso)) {
        $("#indice_masa_corporal").val(parseFloat(peso / Math.pow(talla, 2)).toFixed(2));
    } else {
        $("#indice_masa_corporal").val("");
    }
}