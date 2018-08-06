$(document).ready( function() {
    var imagen_valida = false;

    $(document).on('change', '.btn-file :file', function() {
        var input = $(this);
        if(imagen_valida) {
            $("#mensaje").attr("hidden", "hidden");
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        } else {
            $("#mensaje").removeAttr("hidden");
            label = "";
        }
        input.trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function(event, label) {
        var input = $(this).parents('.input-group').find(':text');
        var log = "";
        if(imagen_valida) {
            log = label;
        }
        if(input.length) {
            input.val(log);
        }
    });

    function readURL(input) {
        var reader = new FileReader();
        if (input.files && input.files[0] && foto_valida(input.files[0])) {
            reader.onload = function (e) {
                $('#foto_empleado').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            $('#foto_empleado').attr('src', '/static/images/cargar_foto.png');
        }
    }

    $("#ingreso_foto").change(function(){
        readURL(this);
    });

    var tipos_archivo = [
        'image/jpg',
        'image/jpeg',
        'image/png'
    ];

    function foto_valida(archivo) {
        for(var i = 0; i < tipos_archivo.length; i++) {
            if(archivo.type === tipos_archivo[i]) {
                imagen_valida = true;
                return true;
            }
        }
        imagen_valida = false;
        return false;
    }

});