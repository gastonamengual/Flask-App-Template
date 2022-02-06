from datetime import datetime

from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import productos_controller, insumos_controller
from ...models.models import Producto, LineaInsumo, PrecioProducto, Insumo

productos_scope = Blueprint('productos_api', __name__, url_prefix='/productos')

@productos_scope.post('/productos')
def producto_dispatcher():
    
    data = request.form.to_dict()

    ### Request Cookies
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
 
    ### Gather Linea Insumos
    insumos_ids = [v for k,v in data.items() if 'id_insum' in k]
    cantidades = [float(v) for k,v in data.items() if 'cant' in k]

    lineas_insumo = []
    for insumo_id, cantidad in zip(insumos_ids, cantidades):
        linea_insumo = {'id_insumo': insumo_id, 'cantidad':float(cantidad)}
        lineas_insumo.append(linea_insumo)
    
    ### Create Producto instance
    producto = Producto(id_ = data.get("id_"),
                        nombre = data['nombre'],
                        stock_minimo = int(data['stock_minimo']),
                        stock_actual=int(data['stock_actual']),
                        costo=float(data['costo']),
                        lineas_insumo = lineas_insumo,)
    
    ### Define Proveedor
    producto.id_proveedor = None if lineas_insumo else data['id_proveedor']

    ### PRECIO PRODUCTO
    precio_producto = PrecioProducto(fecha = datetime.today().strftime('%Y-%m-%d'),
                                     precio = float(data['precio']))

    method = data.get("_method")
    if method == "POST":
        return producto_crear(producto, precio_producto, usuario_id, emprendimiento_id)
    elif method == "PUT":
        return producto_editar(producto, precio_producto, usuario_id, emprendimiento_id)
    elif method == "DELETE":
        return producto_borrar(producto, usuario_id, emprendimiento_id)
    else:
        raise ValueError("Producto received an invalid method")

######## CREAR ########
def producto_crear(producto, precio_producto, usuario_id, emprendimiento_id):
    productos_controller.create(producto, precio_producto, usuario_id, emprendimiento_id)
    flash('Producto creado con éxito!')
    return redirect(url_for('views.productos_views.productos'))

######## EDITAR ########
def producto_editar(producto, precio_producto, usuario_id, emprendimiento_id):
    productos_controller.edit(producto, precio_producto, usuario_id, emprendimiento_id)
    flash('Producto editado con éxito!')
    return redirect(url_for('views.productos_views.productos'))

#### BORRAR
@productos_scope.post('/producto_borrar')
def producto_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    producto_id = data.get("delete_id")
    producto_ = Producto(id_=producto_id)
    producto = productos_controller.get_by_id(producto_, usuario_id, emprendimiento_id)

    productos_controller.delete(producto, usuario_id, emprendimiento_id)

    flash('Producto borrado con éxito!')
    return redirect(url_for('views.productos_views.productos'))