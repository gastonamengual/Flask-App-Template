$(document).ready(function() {

    //////////// BORRAR Producto ////////////
    /// Fill and open editar modal
    function borrar_modal(producto){
        $("[name='delete_id']").val(producto.id_)
        $("#modal-borrar").modal();
    }

    /// Get producto to delete
    $('[id*="borrar-producto"]').click(function(){

        var producto_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/productos/borrar/",
            type: "post",
            data: {'producto_id': producto_id},
            success: function(producto) {
                borrar_modal(producto);
            }
        });
    });

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
      $("#modal-productos").modal();
    }

    // MOSTRAR INSUMOS
    $('[id^="detalle"]').click(function() {
        table_num = this.id.replace( /^\D+/g, '')
        table_id = "#tableLineaProducto" + table_num
        $('[id^="tableLineaProducto"]').each(function() {
            if (this.id != table_id){
                $(this).css("display", "none");
            } 
            
        })
        $(table_id).css("display", "flex")
        $(table_id).css("justify-content", "center")
        $(table_id).css("align-items", "center")
        $(table_id).css("flex-direction", "column")
        $("#modal-producto-detalle").modal();
    });

    // DATA TABLES
    $('#productTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "asc" ]],
        columnDefs: [
            { orderable: false, targets: 5 },
            { orderable: false, targets: 6 },
            { orderable: false, targets: 7 }
          ]
    });
    $('.dataTables_length').addClass('bs-select');
   
});

/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
  "language": {
      "decimal": ".",
      "thousands": ",",
      "info": "_TOTAL_ productos registrados",
      "infoEmpty": "No hay productos.",
      "search": "Buscar:",
      "searchPlaceholder": "Ingresa por cualquier campo",
      "zeroRecords": "No se encontraron resultados",
      "emptyTable": "No se han registrado productos.",
  }            
} );