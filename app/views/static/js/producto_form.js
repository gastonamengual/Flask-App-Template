$(document).ready(function() {

    calculate_fields()

    // OPEN MODAL IF MESSAGES
    if ($('#flashes').children().length > 0){
        $("#modal-productos-form").modal();
    }

    /// Verify remove proveedor
    number_linea_insumos = $('#agregar-insumo-form').children('.row').length;
    if (number_linea_insumos > 0){
        hideFields();
    } else{
        showFields();
    }

    /// Open modal if proveedores select is clicked and empty
    $("#id_proveedor").focus(function(){
        if ($('#id_proveedor > option').length == 1){
            $("#modal-productos-form").modal();
        }
    });

    //////// Agregar Linea Insumo
    $("#add_insumo").click(function() {

        agregar_linea_insumo()

        // Verify remove proveedor
        number_linea_insumos = $('#agregar-insumo-form').children('.row').length;
        if (number_linea_insumos > 0){
            hideFields();
        }

    });

    /////// Remove Linea
    $(".remove-linea").click(function() {
        $(this).parent().parent().parent().remove();

        // Verify remove proveedor
        number_linea_insumos = $('#agregar-insumo-form').children('.row').length;
        if (number_linea_insumos == 0){
            showFields();
        }
    });

    //////// Delete storage
    $("#finalizar").click(function() {
        $('#agregar-insumo-storage').remove();
    });

});

function hideFields(){
    $("#id_proveedor").prop('disabled', true);
    $("#id_proveedor").attr('required', false);
    $("#id_proveedor").prop("selectedIndex", 0);
    $("#stock_actual").prop('readonly', true);
    $("#stock_actual").attr('required', false);
    $("#costo").prop('readonly', true);
    $("#costo").attr('required', false);
    $("#precio").prop('readonly', true);
    $("#precio").attr('required', false);
}

function showFields(){
    $("#id_proveedor").prop('disabled', false);
    $("#id_proveedor").attr('required', true);
    $("#stock_actual").prop('readonly', false);
    $("#stock_actual").attr('required', true);
    $("#costo").prop('readonly', false);
    $("#costo").attr('required', true);
    $("#precio").prop('readonly', false);
    $("#precio").attr('required', true);
}

function calculate_fields(){
    
    insumos = []
    $('[name^="id_insumo"] option:selected').each(function(){
        insumos.push($(this).attr('id'));
    });

    cantidades = [];
    $('[name^="cantidad"]').each(function(){
        cantidades.push(parseFloat($(this).val()));
    });

    $.ajax({
        url: "/productos/calculate_fields/",
        type: "post",
        data: {'insumos': insumos, 'cantidades': cantidades},
        success: function(fields) {
            $('#stock_actual').val(fields[0])
            $('#stock_actual_label').addClass('label-active')
            $('#costo').val(fields[1])
            $('#costo_label').addClass('label-active')
            $('#precio').val(fields[2])
            $('#precio_label').addClass('label-active')
        }
    });
}

function agregar_linea_insumo(){
    /// Get all insumos from storage
    var insumo_list = [];
    $("#agregar-insumo-storage option").each(function(){
        insumo_list.push($(this).clone());
    });

    /// Open modal if no insumos
    if (insumo_list.length == 0){
        $("#modal-productos-form").modal();
    }

    /// Get last div and calculate next id
    var last_id = $('[id*="agregar-insumo-field"]').last().attr('id')
    if (last_id === undefined){
        var next_id = 0
    } else{
        var last_id = parseInt(last_id.replace( /^\D+/g, ''));
        var next_id = last_id + 1; 
    }

    /// Create div
    var row = $("<div class=\"row\" id=\"agregar-insumo-field" + next_id + "\"/>");
    row.data("idx", next_id);

    // INSUMO
    var col1 = $("<div class=\"md-form col-6\"/>");
    var select = $("<select class=\"browser-default custom-select\" type=\"text\" name=\"id_insumo"+next_id+"\" required>");
    insumo_list.forEach(element => {
        select.append(element)
    });
    col1.append(select)

    // CANTIDAD
    var col2 = $("<div class=\"md-form col-4\"/>");
    var label = $("<label class=\"form-label\" />Cantidad</label>");
    var cantidad = $("<input class=\"form-input\" type=\"number\" name=\"cantidad"+next_id+"\" min=0 step=0.01 / required>");
    col2.append(label)
    col2.append(cantidad)

    cantidad.change(function() {
        calculate_fields();
    });
    select.change(function() {
        calculate_fields();
    });

    // REMOVE BUTTON
    var col3 = $("<div class=\"md-form col-2\"/>");
    var removeButton = $("<input class=\"btn btn-danger btn-sm remove-linea\" value=\"X\" style=\"width: 10%;\"/>");
    col3.append(removeButton)

    removeButton.click(function() {
        $(this).parent().parent().remove();
        number_linea_insumos = $('#agregar-insumo-form').children('.row').length;
        if (number_linea_insumos == 0){
            showFields();
        }
    });

    row.append(col1);
    row.append(col2);
    row.append(col3);
    $("#agregar-insumo-form").append(row);

    row.find("span").remove();
}