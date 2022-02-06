$(document).ready(function() {

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-alert").modal();
    }

    //////////// CREAR CLIENTE ////////////
    $("#crear-emprendimiento").click(function(){
        $("#modal-crear-form").modal();
    });

    //////////// EDITAR CLIENTE ////////////
    /// Fill and open editar modal
    function editar_modal(emprendimiento){
        $("[name='id_']").val(emprendimiento.id_)
        $("[name='nombre']").val(emprendimiento.nombre)
        $("[name='margen_ganancia']").val(emprendimiento.margen_ganancia)
        $("#modal-editar-form").modal();
    }

    /// Get emprendimiento to edit
    $('[id*="editar-emprendimiento"]').click(function(){

        var emprendimiento_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/emprendimientos/editar/",
            type: "post",
            data: {'emprendimiento_id': emprendimiento_id},
            success: function(emprendimiento) {
                editar_modal(emprendimiento);
            }
        });
    });

    //////////// BORRAR CLIENTE ////////////
    /// Fill and open editar modal
    function borrar_modal(emprendimiento){
        $("[name='delete_id']").val(emprendimiento.id_)
        $("#modal-borrar").modal();
    }

    /// Get emprendimiento to delete
    $('[id*="borrar-emprendimiento"]').click(function(){

        var emprendimiento_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/emprendimientos/borrar/",
            type: "post",
            data: {'emprendimiento_id': emprendimiento_id},
            success: function(emprendimiento) {
                borrar_modal(emprendimiento);
            }
        });
    });

});