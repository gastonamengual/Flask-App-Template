$(document).ready(function() {

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-error").modal();
    }
    
    agregar_linea_venta()

    //////// ADD LINEA DE INSUMO
    $("#add_producto").click(function() {
        agregar_linea_venta()
    });

    /////// REMOVE LINEA BUTTON
    $(".remove-linea").click(function() {
        $(this).parent().parent().parent().remove();
    });

    //////// ELIMINAR LINEA INSUMO 0
    $("#finalizar").click(function() {
        $('#agregar-producto-storage').remove();
    });

    //////// VENTA - HIDE AND SHOW VENTA WHEN CLICK ARROW
    $('[id^="detalle"]').click(function() {
        table_num = this.id.replace( /^\D+/g, '')
        table_id = "#tableLineaVenta" + table_num
        $('[id^="tableLineaVenta"]').each(function() {
            if (this.id != table_id){
                $(this).css("display", "none");
            } 
            
        })
        $(table_id).css("display", "block")
        $("#modal-venta-detalle").modal();
    });

    ////// FINALIZAR VENTA
    $('#finalizar-venta').click(function() {
        finalizar_venta()
    });

    ////// DATA TABLES
    $('#crearVentaTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "sort": false,
        "searching": false,
    });
    $('.dataTables_length').addClass('bs-select');

    $('#ventasTable').DataTable({
        "scrollY": "400px",
        "scrollCollapse": true,
        "paging": false,
        "order": [[ 0, "desc" ]],
        columnDefs: [
            { orderable: false, targets: 3 }
          ]
    });
    $('.dataTables_length').addClass('bs-select');
});

/// DATA TABLES IN SPANISH
$.extend( true, $.fn.dataTable.defaults, {
    "language": {
        "decimal": ".",
        "thousands": ",",
        "info": "_TOTAL_ ventas registradas",
        "infoEmpty": "No hay ventas.",
        "search": "Buscar:",
        "searchPlaceholder": "Ingresa por cualquier campo",
        "zeroRecords": "No se encontraron resultados",
        "emptyTable": "No se han registrado ventas.",
    }            
} );

///////////////////////////////////////////////////////////
function calculate_total_price(){
    productos = []
    $('[name^="producto"] option:selected').each(function(){
        productos.push($(this).text());
    });

    $.ajax({
        url: "/ventas/ventas_precios/",
        type: "post",
        data: {'productos': productos},
        success: function(precios) {
            
            cantidades = [];
            $('[name^="cantidad"]').each(function(){
                cantidades.push(parseInt($(this).val()));
            });
            
            subtotales = [];
            for (let i = 0; i < Math.min(precios.length, cantidades.length); i++) {
                subtotales[i] = precios[i] * cantidades[i];
            }
            
            $('[name^="subtotal"]').each(function(i){
                $(this).text(subtotales[i]);
            });

            var total = subtotales.reduce((partial_sum, a) => partial_sum + a, 0);
            $('#total').text('Total: $' + total)
        }
    });
}

///////////////////////////////////////////////////////////
function validate_max_stock(element){
    var cantidad = element.val()
    var rowId = $(element).attr('name').replace( /^\D+/g, '')
    var producto_nombre = $('[name="producto' + rowId + '"] option:selected').text()
    if (producto_nombre != 'Elegir producto'){
        $.ajax({
            url: "/ventas/validate_max_stock/",
            type: "post",
            data: {'producto_nombre': producto_nombre},
            success: function(producto) {
                $('#stock' + rowId).text(producto.stock_actual)
                if (cantidad > producto.stock_actual){
                    $('#modal-alert-text').text('La cantidad máxima para ' + producto_nombre + ' es ' + producto.stock_actual)
                    $("#modal-alert").modal();
                    element.val(0)
                }
            },
            async: false
        });
    }
}

///////////////////////////////////////////////////////////
function agregar_linea_venta(){
    
    var producto_list = [];
    $("#agregar-linea-storage option").each(function(){
        producto_list.push($(this).clone());
    });
    
    /// Get last div and calculate next id
    var last_id = $('[id*="agregar-linea-field"]').last().attr('id')
    if (last_id === undefined){
        var next_id = 0
    } else{
        var last_id = parseInt(last_id.replace( /^\D+/g, ''));
        var next_id = last_id + 1; 
    }
    
    ///////// COL1 PRODUCTO LIST
    var td1 = $("<td/>");
    var select = $("<select class=\"browser-default custom-select\" type=\"text\" name=\"producto"+next_id+"\" required>");
    producto_list.forEach(element => {
        select.append(element)
    });
    td1.append(select)
    
    ///////// COL2 CANTIDAD
    var td2 = $("<td/>");
    var button_minus = $("<p class=\"btn btn-link px-2\" onclick=\"this.parentNode.querySelector('input[type=number]').stepDown()\" />");
    var icon_minus = $("<i class=\"fas fa-minus\" />");
    
    var cantidad = $("<input class=\"form-input\" style=\"width: 25%;\" type=\"number\" name=\"cantidad"+next_id+"\" value=\"1\" min=0 / required>");
    
    var button_plus = $("<p class=\"btn btn-link px-2\" onclick=\"this.parentNode.querySelector('input[type=number]').stepUp()\" />");
    var icon_plus = $("<i class=\"fas fa-plus\" />");
    
    button_minus.append(icon_minus)
    button_plus.append(icon_plus)
    td2.append(button_minus)
    td2.append(cantidad)
    td2.append(button_plus)
    
    cantidad.change(function() {
        calculate_total_price();
        validate_max_stock(cantidad);
    });
    button_minus.click(function() {
        calculate_total_price();
        validate_max_stock(cantidad);
    });
    button_plus.click(function() {
        calculate_total_price();
        validate_max_stock(cantidad);
    });
    
    select.change(function() {
        calculate_total_price();
        validate_max_stock(cantidad);
    });
    
    ////////// COL3 SUBTOTAL
    var td3 = $("<td id=\"stock"+next_id+"\" />");
    
    ////////// COL3 SUBTOTAL
    var td4 = $("<td/>");
    var subtotal = $("<p name=\"subtotal"+next_id+"\" />");
    td4.append(subtotal)
    
    ///////// COL4 REMOVE BUTTON
    var td5 = $("<td/>");
    if (next_id > 0){
        var removeButton = $("<input type=\"button\" class=\"btn btn-danger btn-sm remove-linea\" value=\"X\" />");
        td5.append(removeButton)
        
        removeButton.click(function() {
            $(this).parent().parent().remove();
            calculate_total_price();
        });
    }
    
    ////////// TABLE ROW
    var row = $("<tr id=\"agregar-linea-field" + next_id + "\"/>");
    row.data("idx", next_id);
    row.append(td1);
    row.append(td2);
    row.append(td3);
    row.append(td4);
    row.append(td5);
    $("#agregar-linea-form").append(row);
    
    ///// Calculate total price
    calculate_total_price()
}

///////////////////////////////////////////////////////////
function finalizar_venta(){
    var condition1 = false;
    var condition2 = false;
    var condition3 = false;
    var condition4 = false;
    
    /// Cantidad non zero
    $('[name^="cantidad"]').each(function(){
        if (parseInt($(this).val()) <= 0){
            $('#modal-alert-text').text('La cantidad debe ser al menos 1')
            $("#modal-alert").modal(); 
        } else {condition1 = true;}
    });

    /// DNI no incompleto
    dni = $('[name="dni_cliente"]').val()
    if (dni == ""){
        $('#modal-alert-text').text('Debe ingresar el dni de un cliente')
        $("#modal-alert").modal();
    } else {condition2 = true;}

    /// Validate dni exists
    $.ajax({
        url: "/ventas/ventas_validate_dni/",
        type: "post",
        data: {'dni': dni},
        success: function(cliente) {
            if (cliente == null){
                $('#modal-alert-text').text('El cliente no existe')
                $("#modal-alert").modal();
            } else {condition3 = true;}
        },
        async: false
    });

    /// Productos no vacíos
    $('[name^="producto"]').each(function(){
        if ($(this).val() == null){
            $('#modal-alert-text').text('Debe elegir un producto')
            $("#modal-alert").modal();
        } else {condition4 = true;}
    });

    if (condition1 && condition2 && condition3 && condition4){
        productos = []
        $('[name^="producto"] option:selected').each(function(){
            productos.push($(this).text());
        });
        cantidades = [];
        $('[name^="cantidad"]').each(function(){
            cantidades.push(parseInt($(this).val()));
        });

        total = $("#total").text().replace( /^\D+/g, '')

        $.ajax({
            url: "/ventas/finalizar_venta/",
            type: "post",
            data: {'productos': productos, 'cantidades': cantidades, 'dni': [dni], 'total': [total]},
            success: function() {
                $('[id^="agregar-linea-field"]').each(function(){
                    $(this).remove();
                    $('#total').text('');
                    agregar_linea_venta();
                    $('[name="dni_cliente"]').val('')
                    $('#modal-alert-text').text('Venta registrada!')
                    $("#modal-alert").modal();
                });
            },
            async: false
        });
    }
}