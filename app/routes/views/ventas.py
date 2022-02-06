from datetime import datetime
from math import ceil

from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from ...controllers import ventas_controller, clientes_controller, productos_controller, emprendimientos_controller, insumos_controller
from ...models.exceptions import NoEntitiesRegistered
from ...models.models import Emprendimiento, Cliente, LineaVenta, Venta

ventas_scope = Blueprint('ventas_views', __name__, url_prefix='/ventas')

#### VENTA
@ventas_scope.get("/")
def crear_ventas():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Clientes
    try:
        clientes = clientes_controller.get_all(usuario_id, emprendimiento_id)
    except:
        flash("Debe registrar clientes para poder vender")
        return redirect(url_for('views.emprendimientos_views.emprendimiento_home', id=emprendimiento.id_))

    ### Productos
    try:
        productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    except:
        flash("Debe registrar productos para poder vender")
        return redirect(url_for('views.emprendimientos_views.emprendimiento_home', id=emprendimiento.id_))

    tiene_stock = []
    for producto in productos:
        if producto.stock_actual == 0:
            tiene_stock.append('si')
        else:
            tiene_stock.append('no')

    return render_template("emprendimientos/ventas/ventas.html", 
                           clientes=clientes,
                           emprendimiento=emprendimiento,
                           productos_stock=zip(productos, tiene_stock))

#### VENTAS PRECIOS (desde ajax)
@ventas_scope.post("/ventas_precios/")
def ventas_precios():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    productos_list = request.form.getlist('productos[]')

    productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    precios = []
    for producto_list in productos_list:
        for producto in productos:
            if producto.nombre == producto_list:
                precio_producto = productos_controller.get_last_precio(producto, usuario_id, emprendimiento_id)
                precios.append(precio_producto.precio)

    return jsonify(precios)

#### VALIDATE DNI (desde ajax)
@ventas_scope.post("/ventas_validate_dni/")
def ventas_validate_dni():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    dni = str((list(data.values()))[0])
    cliente_ = Cliente(dni=dni)
    cliente = clientes_controller.get_by_dni(cliente_, usuario_id, emprendimiento_id)

    return jsonify(cliente)

#### VALIDATE MAX STOCK (desde ajax)
@ventas_scope.post("/validate_max_stock/")
def validate_max_stock():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    producto_nombre = list(data.values())[0]
    productos = productos_controller.get_all(usuario_id, emprendimiento_id)

    for producto in productos:
        if producto.nombre == producto_nombre:
            return jsonify(producto)

#### LISTA VENTAS
@ventas_scope.get("/lista_ventas")
def lista_ventas():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get Ventas
    try:
        ventas = ventas_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        flash("No hay ventas registradas")
        return crear_ventas()

    clientes_ = clientes_controller.get_all(usuario_id, emprendimiento_id)
    
    clientes = []
    for venta in ventas:
        # venta.fecha = datetime.strptime(venta.fecha, '%Y-%m-%d').strftime('%d/%m/%Y')
        for cliente in clientes_:
            if cliente.dni == venta.dni_cliente:
                clientes.append(cliente)

    productos = productos_controller.get_all(usuario_id, emprendimiento_id)

    precios = []
    for producto in productos:
        precio = productos_controller.get_last_precio(producto, usuario_id, emprendimiento_id)
        precios.append(precio.precio)


    return render_template("emprendimientos/ventas/lista_ventas.html",
                            emprendimiento=emprendimiento, 
                            ventas_cliente=list(zip(ventas, clientes)),
                            productos_precios=list(zip(productos,precios)))


#### VENTAS FINALIZAR (desde ajax)
@ventas_scope.post("/finalizar_venta/")
def finalizar_venta():
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    productos_nombres = request.form.getlist('productos[]')
    cantidades = request.form.getlist('cantidades[]')
    dni_cliente = request.form.getlist('dni[]')[0]
    total = request.form.getlist('total[]')[0]

    productos = productos_controller.get_all(usuario_id, emprendimiento_id)

    ### Lista de productos vendidos
    productos_vendidos = []
    for producto_nombre in productos_nombres:
        for producto in productos:
            if producto.nombre == producto_nombre:
                productos_vendidos.append(producto)

    ### Creación de LineasVenta
    lineas_venta = []
    for producto, cantidad in zip(productos_vendidos, cantidades):
        linea_venta = LineaVenta(cantidad=int(cantidad), id_producto=producto.id_)
        lineas_venta.append(linea_venta)
    
    venta = Venta(id_ = None,
                  fecha = datetime.today().strftime('%Y-%m-%d'),
                  dni_cliente = dni_cliente,
                  total = float(total),
                  lineas_venta = lineas_venta,
    )
    venta = ventas_controller.create(venta, usuario_id, emprendimiento_id)

    # Actualizar stock de insumos
    insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
    
    for insumo in insumos:
        cantidad_usada = 0
        for producto, cantidad in zip(productos_vendidos, cantidades):
            for linea_insumo in producto.lineas_insumo:
                if insumo.id_ == linea_insumo['id_insumo']:
                    cantidad_usada += linea_insumo['cantidad'] * int(cantidad)
        if cantidad_usada > 0:
            insumo.stock_actual_en_medida = max(insumo.stock_actual_en_medida - cantidad_usada, 0)
            insumo.stock_actual = ceil(insumo.stock_actual_en_medida / insumo.medida_presentacion)
            insumos_controller.edit(insumo, usuario_id, emprendimiento_id)

    # Actualizar stock de precios
    for producto_ in productos_vendidos:
        producto = productos_controller.calculate_stock(producto_, usuario_id, emprendimiento_id)
        productos_controller.edit(producto, None, usuario_id, emprendimiento_id)

    return 'success'