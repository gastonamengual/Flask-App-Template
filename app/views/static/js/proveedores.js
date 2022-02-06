$(document).ready(function() {

    //////////// CREAR PROVEEDOR ////////////
    $("#crear-proveedor").click(function(){
        $("[name='_method']").val("POST")
        $("[name='nombre']").val('')
        $("[name='telefono']").val('')
        $("#finalizar").text("Crear proveedor")
        $("#modal-proveedor-form").modal();
    });

    //////////// EDITAR PROVEEDOR ////////////
    /// Fill and open editar modal
    function editar_modal(proveedor){
        $("[name='_method']").val("PUT")
        $("[name='id_']").val(proveedor.id_)
        $("[name='nombre']").val(proveedor.nombre)
        $("[name='telefono']").val(proveedor.telefono)
        $("#finalizar").text("Editar proveedor")
        $("#modal-proveedor-form").modal();
    }

    /// Get proveedor to edit
    $('[id*="editar-proveedor"]').click(function(){

        var proveedor_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/proveedores/editar/",
            type: "post",
            data: {'proveedor_id': proveedor_id},
            success: function(proveedor) {
                editar_modal(proveedor);
            }
        });
    });

    //////////// BORRAR PROVEEDOR ////////////
    /// Fill and open editar modal
    function borrar_modal(proveedor){
        $("[name='delete_id']").val(proveedor.id_)
        $("#modal-borrar").modal();
    }

    /// Get proveedor to delete
    $('[id*="borrar-proveedor"]').click(function(){

        var proveedor_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/proveedores/borrar/",
            type: "post",
            data: {'proveedor_id': proveedor_id},
            success: function(proveedor) {
                borrar_modal(proveedor);
            }
        });
    });

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-error").modal();
        $("#modal-lista-productos").modal();
    }

    // DATA TABLES
    $('#proveedoresTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "asc" ]],
        columnDefs: [
            { orderable: false, targets: 2 },
            { orderable: false, targets: 3 },
            { orderable: false, targets: 4 },
            { orderable: false, targets: 5 },
          ]
    });
    $('.dataTables_length').addClass('bs-select');
    
    $('#proveedorProductsTable').DataTable({
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
        "info": "_TOTAL_ proveedores registrados",
        "infoEmpty": "No hay proveedores.",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "No se encontraron resultados",
        "emptyTable": "No se han registrado proveedores.",
    }            
  } );