from datetime import datetime

from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import pedidos_controller, insumos_controller, productos_controller
from ...models.models import Pedido, LineaPedido

pedidos_scope = Blueprint('pedidos_api', __name__, url_prefix='/pedidos')

### CREAR PEDIDO
@pedidos_scope.post('/pedidos')
def crear_pedido():

    data = request.form.to_dict()
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    ### Lineas Pedido
    articulos_ids = [v for k,v in data.items() if 'articulo' in k]
    cantidades = [v for k,v in data.items() if 'cantidad' in k]

    lineas_pedido = []
    for articulo_id, cantidad in zip(articulos_ids, cantidades):
        linea_pedido = LineaPedido(
                cantidad = int(cantidad),
                id_articulo = articulo_id,)
        lineas_pedido.append(linea_pedido)


    ### Pedido
    pedido = Pedido(id_ = None,
                    fecha_confeccion = datetime.today().strftime('%Y-%m-%d'),
                    fecha_recepcion = None,
                    id_proveedor = data.get("id_proveedor"),
                    estado = 'pendiente',
                    lineas_pedido = lineas_pedido,
    )

    pedido = pedidos_controller.create(pedido, usuario_id, emprendimiento_id)

    flash('Pedido creado con éxito')
    return redirect(url_for('views.proveedores_views.proveedores'))


#### MARCAR RECIBIDO
@pedidos_scope.post("/pedidos/marcar_recibido")
def marcar_recibido():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    # Pedido
    data = request.form.to_dict()
    id_pedido = data['id_pedido']
    pedido_ = Pedido(id_=id_pedido)
    pedido = pedidos_controller.get_by_id(pedido_, usuario_id, emprendimiento_id)
    
    # Modificar pedido
    pedido.estado = 'recibido'
    pedido.fecha_recepcion = datetime.today().strftime('%Y-%m-%d')
    pedidos_controller.edit(pedido, usuario_id, emprendimiento_id)

    # Actualizar stock de articulos pedidos
    insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
    productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    articulos = insumos + productos

    for linea_pedido in pedido.lineas_pedido:
        for articulo in articulos:
            if linea_pedido['id_articulo'] == articulo.id_:
                articulo.stock_actual += linea_pedido['cantidad']
                if type(articulo).__name__ == 'Insumo':
                    insumos_controller.edit(articulo, usuario_id, emprendimiento_id)
                else:
                    productos_controller.edit(articulo, usuario_id, emprendimiento_id)

    # Actualizar stock de productos segun nuevos insumos
    if insumos:
        for producto in productos:
            producto = productos_controller.calculate_stock(producto, usuario_id, emprendimiento_id)
            productos_controller.edit(producto, None, usuario_id, emprendimiento_id)


    return redirect(url_for('views.pedidos_views.lista_pedidos', proveedor_id=pedido.id_proveedor))

#### MARCAR PENDIENTE
@pedidos_scope.post("/pedidos/marcar_pendiente")
def marcar_pendiente():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    id_pedido = data['id_pedido']
    pedido_ = Pedido(id_=id_pedido)
    pedido = pedidos_controller.get_by_id(pedido_, usuario_id, emprendimiento_id)
    pedido.estado = 'pendiente'
    pedidos_controller.edit(pedido, usuario_id, emprendimiento_id)

    return redirect(url_for('views.pedidos_views.lista_pedidos', proveedor_id=pedido.id_proveedor))

#### MARCAR CANCELADO
@pedidos_scope.post("/pedidos/marcar_cancelado")
def marcar_cancelado():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    id_pedido = data['id_pedido']
    pedido_ = Pedido(id_=id_pedido)
    pedido = pedidos_controller.get_by_id(pedido_, usuario_id, emprendimiento_id)
    pedido.estado = 'cancelado'
    pedidos_controller.edit(pedido, usuario_id, emprendimiento_id)

    return redirect(url_for('views.pedidos_views.lista_pedidos', proveedor_id=pedido.id_proveedor))