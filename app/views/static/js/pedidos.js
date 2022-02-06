$(document).ready(function() {

    //////// ADD LINEA DE INSUMO
    $("#add_articulo").click(function() {
        agregar_linea_pedido()
    });

    /////// REMOVE LINEA BUTTON
    $(".remove-linea").click(function() {
        $(this).parent().parent().remove();
    });

    //////// ELIMINAR LINEA INSUMO 0
    $("#finalizar").click(function() {
        $('#crear-articulo-storage').remove();
    });

    //////// PEDIDO - HIDE AND SHOW PEDIDO WHEN CLICK ARROW
    $('[id^="detalle"]').click(function() {
        table_num = this.id.replace( /^\D+/g, '')
        table_id = "#tableLineaPedido" + table_num
        $('[id^="tableLineaPedido"]').each(function() {
            if (this.id != table_id){
                $(this).css("display", "none");
            } 
            
        })
        $(table_id).css("display", "flex")
        $(table_id).css("justify-content", "center")
        $("#modal-pedido-detalle").modal();
    });

    // SHOW MODAL DISABLED
    $(".disabled").click(function() {
        $("#modal-disabled").modal();
    });

    // MODIFICAR ESTADO
    $('[id^="modificar_estado"]').click(function() {
        var pedido_id = $(this).attr('id').match(/\d+/);
        var accion = $(this).attr('name')
        
        var estado = $("#estado"+pedido_id).text()
        
        if (estado == "recibido"){
            $('#modal-alert-text').text('No se puede modificar el estado de un producto recibido')
            $("#modal-alert").modal();
        } else if (estado == 'pendiente'){
            if (accion == 'pendiente'){
                $('#modal-alert-text').text('El estado del pedido ya es "pendiente"')
                $("#modal-alert").modal();
            } else if (accion == 'cancelado'){
                $("[name='id_pedido']").val(pedido_id);
                $("#modal-marcar-cancelado").modal();
            } else if (accion == 'recibido'){
                $("[name='id_pedido']").val(pedido_id);
                $("#modal-marcar-recibido").modal();
            }
        } else if (estado == 'cancelado'){
            if (accion == 'cancelado'){
                $('#modal-alert-text').text('El estado del pedido ya es "cancelado"')
                $("#modal-alert").modal();
            }  else if (accion == 'pendiente'){
                $("[name='id_pedido']").val(pedido_id);
                $("#modal-marcar-pendiente").modal();
            } else if (accion == 'recibido'){
                $("[name='id_pedido']").val(pedido_id);
                $("#modal-marcar-recibido").modal();
            }
        }
    });

    // DATA TABLES
    $('#pedidosTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "desc" ]],
        columnDefs: [
            { orderable: false, targets: 3 },
            { orderable: false, targets: 4 },
            { orderable: false, targets: 5 },
            { orderable: false, targets: 6 },
          ]
    });
    $('.dataTables_length').addClass('bs-select');

    // DATA TABLES
    $('#crearPedidoTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "searching": false,
        "ordering": false,
        columnDefs: [
            { orderable: false, targets: 0 },
            { orderable: false, targets: 1 },
            { orderable: false, targets: 2 },
            { orderable: false, targets: 3 },
          ]
    });
    $('.dataTables_length').addClass('bs-select');
});

/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
    "language": {
        "decimal": ".",
        "thousands": ",",
        "info": "",
        "infoEmpty": "",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "",
        "emptyTable": "",
    }            
});

///////////////////////////////////////////////////////////
function calculate_stock_actual(element){
    var rowId = $(element).attr('name').replace( /^\D+/g, '')
    var id_proveedor = $("[name='id_proveedor']").val()
    var articulo_nombre = $('[name="articulo' + rowId + '"] option:selected').text()
    if (articulo_nombre != 'Elegir articulo'){
        $.ajax({
            url: "/pedidos/calculate_stock_actual/",
            type: "post",
            data: {'articulo_nombre': articulo_nombre, 'id_proveedor': id_proveedor},
            success: function(articulo) {
                $('#stock' + rowId).text(articulo.stock_actual)
            },
            async: false
        });
    }
}

function agregar_linea_pedido(){

    // Get all articulos from storage
    var pedido_list = [];
    $("#crear-pedido-storage option").each(function(){
        pedido_list.push($(this).clone());
    });

    /// Open modal if no pedidos
    if (pedido_list.length == 0){
        $("#modal-articulos-form").modal();
    }
    
    /// Get last div and calculate next id
    var last_id = $('[id*="crear-pedido-field"]').last().attr('id')
    if (last_id === undefined){
        var next_id = 0
    } else{
        var last_id = parseInt(last_id.replace( /^\D+/g, ''));
        var next_id = last_id + 1; 
    }

    ////////// COL1 ARTICULO LIST
    var td1 = $("<td class=\"text-center\"/>");
    var select = $("<select class=\"browser-default custom-select\" type=\"text\" name=\"articulo"+next_id+"\" required>");
    pedido_list.forEach(element => {
        select.append(element)
    });
    td1.append(select)

    ////////// COL2 CANTIDAD
    var td2 = $("<td class=\"text-center\"/>");
    var cantidad = $("<input class=\"form-input\" type=\"number\" name=\"cantidad"+next_id+"\" min=0 / required>");
    td2.append(cantidad)

    select.change(function() {
        calculate_stock_actual(cantidad);
    });

    ////////// COL3 CANTIDAD
    var td3 = $("<td class=\"text-center\" id=\"stock"+next_id+"\" />");


    ///////// COL4 REMOVE BUTTON
    var td4 = $("<td class=\"text-center\"/>");
    var removeButton = $("<input type=\"button\" style=\"margin: 0; width: 3vw; height: 5vh; padding: 1.2vh; text-align: center;\" class=\"btn btn-danger btn-sm remove-linea\" value=\"X\" />");
    td4.append(removeButton)

    removeButton.click(function() {
        $(this).parent().parent().remove();
        number_linea_pedidos = $('#crear-pedido-form').children('.row').length;
    });

    ////////// TABLE ROW
    var row = $("<tr id=\"crear-pedido-field" + next_id + "\"/>");
    row.data("idx", next_id);
    row.append(td1);
    row.append(td2);
    row.append(td3);
    row.append(td4);
    $("#crear-pedido-form").append(row);
}