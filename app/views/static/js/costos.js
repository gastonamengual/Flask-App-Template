$(document).ready(function() {

    //////////// CREAR COSTO ////////////
    $("#crear-costo").click(function(){
        $("[name='_method']").val("POST")
        $("[name='nombre']").val('')
        $("[name='frecuencia_pago']").val('')
        $("#finalizar").text("Crear costo")
        $("#modal-costo-form").modal();
    });

    //////////// CREAR PAGO ////////////
    $("#agregar-pago").click(function(){
        $("#modal-agregar-pago-form").modal();
    });

    //////////// EDITAR COSTO ////////////
    /// Fill and open editar modal
    function editar_modal(costo){
        $("[name='_method']").val("PUT")
        $("[name='id_']").val(costo.id_)
        $("[name='nombre']").val(costo.nombre)
        $("[name='frecuencia_pago']").val(costo.frecuencia_pago)
        $("#finalizar").text("Editar costo")
        $("#modal-costo-form").modal();
    }

    /// Get costo to edit
    $('[id*="editar-costo"]').click(function(){

        var costo_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/costos/editar/",
            type: "post",
            data: {'costo_id': costo_id},
            success: function(costo) {
                editar_modal(costo);
            },
        });
    });

    //////////// BORRAR COSTO ////////////
    /// Fill and open editar modal
    function borrar_modal(costo){
        $("[name='delete_id']").val(costo.id_)
        $("#modal-borrar").modal();
    }

    /// Get costo to delete
    $('[id*="borrar-costo"]').click(function(){

        var costo_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/costos/borrar/",
            type: "post",
            data: {'costo_id': costo_id},
            success: function(costo) {
                borrar_modal(costo);
            },
            async: false
        });
    });

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-error").modal();
    }

    // DATA TABLES
    $('#costosTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "asc" ]],
        columnDefs: [
            { orderable: false, targets: 2 },
            { orderable: false, targets: 3 },
            { orderable: false, targets: 4 },
          ]
    });
    $('.dataTables_length').addClass('bs-select');

    $('#pagosTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "asc" ]],
    });
    $('.dataTables_length').addClass('bs-select');

});

/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
    "language": {
        "decimal": ".",
        "thousands": ",",
        "info": "_TOTAL_ costos registrados",
        "infoEmpty": "No hay costos.",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "No se encontraron resultados",
        "emptyTable": "No se han registrado costos.",
    }            
  } );