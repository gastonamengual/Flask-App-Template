$(document).ready(function() {

    //////////// CREAR CLIENTE ////////////
    $("#crear-cliente").click(function(){
        $("[name='_method']").val("POST")
        $("[name='dni']").val('')
        $("[name='name']").val('')
        $("[name='telefono']").val('')
        $("#finalizar").text("Crear cliente")
        $("#modal-cliente-form").modal();
    });

    //////////// EDITAR CLIENTE ////////////
    /// Fill and open editar modal
    function editar_modal(cliente){
        $("[name='_method']").val("PUT")
        $("[name='id_']").val(cliente.id_)
        $("[name='dni']").val(cliente.dni)
        $("[name='name']").val(cliente.name)
        $("[name='telefono']").val(cliente.telefono)
        $("#finalizar").text("Editar cliente")
        $("#modal-cliente-form").modal();
    }

    /// Get cliente to edit
    $('[id*="editar-cliente"]').click(function(){

        var cliente_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/clientes/editar/",
            type: "post",
            data: {'cliente_id': cliente_id},
            success: function(cliente) {
                editar_modal(cliente);
            }
        });
    });

    //////////// BORRAR CLIENTE ////////////
    /// Fill and open editar modal
    function borrar_modal(cliente){
        $("[name='delete_id']").val(cliente.id_)
        $("#modal-borrar").modal();
    }

    /// Get cliente to delete
    $('[id*="borrar-cliente"]').click(function(){

        var cliente_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/clientes/borrar/",
            type: "post",
            data: {'cliente_id': cliente_id},
            success: function(cliente) {
                borrar_modal(cliente);
            }
        });
    });

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-error").modal();
    }

    // DATA TABLES
    $('#clientesTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 1, "asc" ]],
        columnDefs: [
            { orderable: false, targets: 3 },
            { orderable: false, targets: 4 }
          ]
    });
    $('.dataTables_length').addClass('bs-select');

});

/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
    "language": {
        "decimal": ".",
        "thousands": ",",
        "info": "_TOTAL_ clientes registrados",
        "infoEmpty": "No hay clientes.",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "No se encontraron resultados",
        "emptyTable": "No se han registrado clientes.",
    }            
  } );