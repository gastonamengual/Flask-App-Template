from flask import Blueprint, render_template, request, flash, jsonify
from itsdangerous import json
from ...controllers import productos_controller, proveedores_controller, insumos_controller, emprendimientos_controller
from ...models.models import Emprendimiento, Producto, PrecioProducto
from ...models.exceptions import NoEntitiesRegistered

productos_scope = Blueprint('productos_views', __name__, url_prefix='/productos')

######## PRODUCTO ########
@productos_scope.get("/")
def productos():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    try:
        productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        productos = []
        flash('Todavía no registraste ningún producto')
    
    precios = []
    proveedores = []
    for producto in productos:
        precio_actualizado = productos_controller.get_last_precio(producto, usuario_id, emprendimiento_id)
        precios.append(precio_actualizado)
        proveedor = productos_controller.get_proveedor_name(producto, usuario_id, emprendimiento_id)
        proveedores.append(proveedor)

    insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)

    return render_template("emprendimientos/productos/productos.html", 
                            lista=list(zip(productos,precios,proveedores)),
                            insumos=insumos,
                            emprendimiento=emprendimiento)

######## CREAR ########
@productos_scope.get("/producto_crear")
def producto_crear():
    
    ### Request cookies
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get all proveedores
    try:
       proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        proveedores = []
        flash('No hay proveedores registrados. Debe registrar alguno si tu producto no posee insumos.')

    ### Get all insumos
    try:
        insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)    
    except NoEntitiesRegistered:
        insumos = []
        flash('No hay insumos registrados. Debe registrar alguno si tu producto posee insumos.')

    ### Create empty Producto and PrecioProducto instances
    producto = Producto()
    precio_producto = PrecioProducto()
    
    return render_template("emprendimientos/productos/producto_crear.html", 
                            method="POST", 
                            emprendimiento=emprendimiento,
                            producto=producto, 
                            precio_producto=precio_producto, 
                            proveedores=proveedores, 
                            insumos=insumos)

######## EDITAR ######## 
@productos_scope.get("/editar/<id>")
def producto_editar(id):
    
    ### Request cookies
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get all insumos
    try:
        insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)    
    except NoEntitiesRegistered:
        insumos = []
        flash('Importante: no hay insumos registrados')

    ### Get all proveedores
    proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)
    
    ### Get Producto and PrecioProducto instances
    producto_ = Producto(id_=id)
    producto = productos_controller.get_by_id(producto_, usuario_id, emprendimiento_id)
    precio_producto = productos_controller.get_last_precio(producto, usuario_id, emprendimiento_id)

    return render_template("emprendimientos/productos/producto_editar.html", 
                            method="PUT",
                            emprendimiento=emprendimiento,
                            producto=producto, 
                            precio_producto=precio_producto, 
                            proveedores=proveedores, 
                            insumos=insumos,
                            lineas_insumos_range = enumerate(producto.lineas_insumo))

#### BORRAR (desde ajax)
@productos_scope.post("/borrar/")
def borrar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    data = request.form.to_dict()
    producto_id = (list(data.values()))[0]
    producto_ = Producto(id_=producto_id)
    producto = productos_controller.get_by_id(producto_, usuario_id, emprendimiento_id)

    return jsonify(producto)


#### CALCULATE FIELDS (desde ajax)
@productos_scope.post("/calculate_fields/")
def calculate_fields():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    insumos = request.form.getlist('insumos[]')
    cantidades = request.form.getlist('cantidades[]')
    
    lineas_insumo = []
    for insumo_id, cantidad in zip(insumos, cantidades):
        if (cantidad != 'NaN'):
            linea_insumo = {'id_insumo': insumo_id, 'cantidad':float(cantidad)}
            lineas_insumo.append(linea_insumo)
    producto = Producto(lineas_insumo=lineas_insumo)
    producto = productos_controller.calculate_stock(producto, usuario_id, emprendimiento_id)
    producto = productos_controller.calculate_costo(producto, usuario_id, emprendimiento_id)
    precio = round(producto.costo * emprendimiento.margen_ganancia, 2)

    return jsonify(producto.stock_actual, producto.costo, precio)