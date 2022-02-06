// COPY UNIDAD TEXT INTO PARAGRAPH
function writeUnidad(unidad) {
    var text=unidad.replace(/ /g,"-");
    document.getElementsByName("unidad_medida_presentacion")[0].innerHTML=text;
}

// COPY PRESENTACION TEXT INTO PARAGRAPH
$(document).ready(function() {
    $("#aclaracionStock").css('display', 'none');
});

function aclararStock(presentacion) {
    $("#aclaracionStock").css('display', 'block');
    $('#aclaracionStock').text('Stock (en ' + presentacion + ')');
}

$(document).ready(function() {

    //////////// BORRAR CLIENTE ////////////
    /// Fill and open editar modal
    function borrar_modal(insumo){
        $("[name='delete_id']").val(insumo.id_)
        $("#modal-borrar").modal();
    }

    /// Get insumo to delete
    $('[id*="borrar-insumo"]').click(function(){

        var insumo_id = $(this).attr('id').match(/\d+/);
        
        $.ajax({
            url: "/insumos/borrar/",
            type: "post",
            data: {'insumo_id': insumo_id},
            success: function(insumo) {
                borrar_modal(insumo);
            }
        });
    });


    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-error").modal();
        $("#modal-insumos-form").modal();
    }

    /// Open modal if proveedores select is clicked and empty
    $("#id_proveedor").focus(function(){
        if ($('#id_proveedor > option').length == 1){
            $("#modal-insumos-form").modal();
        }
    });
    
    // DATA TABLES
    $('#insumosTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "asc" ]],
        columnDefs: [
            { orderable: false, targets: 7 },
            { orderable: false, targets: 8 }
          ]
    });
    $('.dataTables_length').addClass('bs-select');

});


/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
    "language": {
        "decimal": ".",
        "thousands": ",",
        "info": "_TOTAL_ insumos registrados",
        "infoEmpty": "No hay insumos.",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "No se encontraron resultados",
        "emptyTable": "No se han registrado insumos.",
    }            
  } );