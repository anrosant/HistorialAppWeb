function agregarRiesgo(tipo) {
    var containers_tipo_riesgo = $(".container_tipo_riesgo_" + tipo);
    var containers_nombre_riesgo = $(".container_nombre_riesgo_" + tipo);
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_" + tipo);
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).removeAttr("hidden");
    }
    $(containers_tipo_riesgo[0]).clone(false, true).appendTo("#container_riesgos_" + tipo + "es");
    $(containers_nombre_riesgo[0]).clone(false, true).appendTo("#container_riesgos_" + tipo + "es");
    $(botones_eliminar[0]).clone(false, true).appendTo("#container_riesgos_" + tipo + "es");
    $("#boton_mas_riesgo_empresa_" + tipo).appendTo("#container_riesgos_" + tipo + "es");
    ordenarRiesgo(tipo);
}

function eliminarRiesgo(tipo, numero) {
    $("#tipo_riesgo_" + tipo + "_" + numero).parent().remove();
    $("#nombre_riesgo_" + tipo + "_" + numero).parent().remove();
    $("#boton_eliminar_riesgo_" + tipo + "_" + numero).parent().remove();
    var containers_tipo_riesgo = $(".container_tipo_riesgo_" + tipo);
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_" + tipo);
    if(containers_tipo_riesgo.length === 1) {
        $(botones_eliminar[0]).attr("hidden", "");
    }
    ordenarRiesgo(tipo);
}

function ordenarRiesgo(tipo) {
    var containers_tipo_riesgo = $(".container_tipo_riesgo_" + tipo);
    var containers_nombre_riesgo = $(".container_nombre_riesgo_" + tipo);
    var botones_eliminar = $(".boton_eliminar_riesgo_empresa_" + tipo);
    for(var i = 0; i < containers_tipo_riesgo.length; i++) {
        $($(containers_tipo_riesgo[i]).children()[0]).attr('id', 'tipo_riesgo_' + tipo + "_" + (i + 1));
        $($(containers_tipo_riesgo[i]).children()[0]).attr('name', 'tipo_riesgo_' + tipo + "_" + (i + 1));
        $($(containers_tipo_riesgo[i]).children()[0]).attr('onchange', 'escogerTipo(' + (i + 1) + ')');
        $($(containers_nombre_riesgo[i]).children()[0]).attr('id', 'nombre_riesgo_' + tipo + "_" + (i + 1));
        $($(containers_nombre_riesgo[i]).children()[0]).attr('name', 'nombre_riesgo_' + tipo + "_" + (i + 1));
        $($(botones_eliminar[i]).children()[0]).attr('onclick', 'eliminarRiesgo(\'' + tipo + '\', ' + (i + 1) + ')');
        $($(botones_eliminar[i]).children()[0]).attr('id', 'boton_eliminar_riesgo_' + tipo + "_" + (i + 1));
    }
}

function escogerTipo(tipo, numero) {
    var tipo_r = $("#tipo_riesgo_" + tipo + "_" + numero).val();
    var nombre = $("#nombre_riesgo_" + tipo + "_" + numero);
    var opciones = $("#nombre_riesgo_" + tipo + "_" + numero + " option");
    for (var i = 1; i < opciones.length; i++) {
        if ($(opciones[i]).attr("class") !== tipo_r) {
            $(opciones[i]).attr("hidden", "");
            console.log(opciones[i]);
        } else {
            $(opciones[i]).removeAttr("hidden");
        }
    }
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
        $(containers_parentesco_patologia[0]).clone(false, true).appendTo("#container_patologias_" + tipo + "es");
    }
    $(containers_nombre_patologia[0]).clone(false, true).appendTo("#container_patologias_" + tipo + "es");
    $(containers_detalle_patologia[0]).clone(false, true).appendTo("#container_patologias_" + tipo + "es");
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