$( document ).ready(function() {
    $("#menu_sesion").on('hidden.bs.collapse', function () {
        $("#menu_sesion").addClass("d-flex justify-content-end");
    });
});