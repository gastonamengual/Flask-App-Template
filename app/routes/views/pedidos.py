from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from ...controllers import pedidos_controller, proveedores_controller, productos_controller, insumos_controller, emprendimientos_controller
from ...models.exceptions import NoEntitiesRegistered
from ...models.models import Emprendimiento, Proveedor

pedidos_scope = Blueprint('pedidos_views', __name__, url_prefix='/pedidos')

#### LISTA PEDIDOS
@pedidos_scope.get("/pedidos/<proveedor_id>")
def lista_pedidos(proveedor_id):

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get proveedor
    proveedor_ = Proveedor(id_=proveedor_id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)

    ### Get pedidos of proveedor
    try:
        pedidos = pedidos_controller.get_by_proveedor(usuario_id, emprendimiento_id, proveedor_id)
    except NoEntitiesRegistered:
        flash('Todavía no registraste ningún pedido para este proveedor')
        return redirect(url_for('views.proveedores_views.proveedores'))

    try:
        insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        insumos = []
    
    try:
        productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        productos = []

    articulos = insumos + productos

    ### Get nombre of articulos in lineas pedido
    for pedido in pedidos:
        for linea_pedido in pedido.lineas_pedido:
            for articulo in articulos:
                if linea_pedido['id_articulo'] == articulo.id_:
                    linea_pedido['nombre_articulo'] = articulo.nombre

    return render_template("emprendimientos/pedidos/lista_pedidos.html", 
                           emprendimiento=emprendimiento,
                           pedidos=pedidos, 
                           proveedor=proveedor)

#### CALCULATE STOCK ACTUAL (desde ajax)
@pedidos_scope.post("/calculate_stock_actual/")
def calculate_stock_actual():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    id_proveedor = data['id_proveedor']
    articulo_nombre = data['articulo_nombre']

    proveedor_ = Proveedor(id_=id_proveedor)
    articulos = proveedores_controller.get_articulos(proveedor_, usuario_id, emprendimiento_id)

    for articulo in articulos:
        if articulo.nombre == articulo_nombre:
            return jsonify(articulo)

#### CREAR PEDIDO
@pedidos_scope.get("/pedidos/crear_pedido/<proveedor_id>")
def crear_pedido(proveedor_id):
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get proveedor
    proveedor_ = Proveedor(id_=proveedor_id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)
    
    ### Get articulos of proveedor
    try:
        articulos = proveedores_controller.get_articulos(proveedor, usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        flash('Todavía no registraste ningún articulo o insumo para este proveedor')
        return redirect(url_for('views.proveedores_views.proveedores'))

    ### Get articulos con stock bajo
    stock_bajo = []
    for articulo in articulos:
        if articulo.stock_actual < articulo.stock_minimo:
            stock_bajo.append(articulo)

    return render_template('emprendimientos/pedidos/pedido_crear.html',
                            emprendimiento=emprendimiento,
                            articulos=articulos,
                            proveedor=proveedor,
                            stock_bajo=enumerate(stock_bajo))