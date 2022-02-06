from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import insumos_controller, productos_controller
from ...models.models import Insumo

insumos_scope = Blueprint('insumos_api', __name__, url_prefix='/insumos')

@insumos_scope.post('/insumos')
def insumo_dispatcher():
    data = request.form
    method = data.get("_method")

    insumo = Insumo(id_ = data.get("id_"),
                    nombre = data['nombre'],
                    id_proveedor = data['id_proveedor'],
                    unidad = data['unidad'],
                    presentacion = data['presentacion'],
                    medida_presentacion = int(data['medida_presentacion']),
                    stock_actual = int(data['stock_actual']),
                    stock_actual_en_medida = float(int(data['stock_actual']) * int(data['medida_presentacion'])),
                    costo = float(data['costo']),
                    stock_minimo = int(data['stock_minimo']),)
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    if method == "POST":
        return insumo_crear(insumo, usuario_id, emprendimiento_id)
    elif method == "PUT":
        return insumo_editar(insumo, usuario_id, emprendimiento_id)
    elif method == "DELETE":
        return insumo_borrar(insumo, usuario_id, emprendimiento_id)
    else:
        raise ValueError("Insumo received an invalid method")

#### CREAR
def insumo_crear(insumo, usuario_id, emprendimiento_id):
    insumos_controller.create(insumo, usuario_id, emprendimiento_id)
    flash('Insumo creado con éxito!')
    return redirect(url_for('views.insumos_views.insumos'))

#### EDITAR
def insumo_editar(insumo, usuario_id, emprendimiento_id):
    insumos_controller.edit(insumo, usuario_id, emprendimiento_id)
    flash('Insumo editado con éxito!')
    return redirect(url_for('views.insumos_views.insumos'))

#### BORRAR
@insumos_scope.post('/insumo_borrar')
def insumo_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    insumo_id = data.get("delete_id")
    insumo_ = Insumo(id_=insumo_id)
    insumo = insumos_controller.get_by_id(insumo_, usuario_id, emprendimiento_id)

    ### Borrar insumos de precios
    insumos_controller.delete(insumo, usuario_id, emprendimiento_id)
    productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    for producto in productos:
        for linea_insumo in producto.lineas_insumo:
            if linea_insumo['id_insumo'] == insumo.id_:
                del linea_insumo['id_insumo']
                del linea_insumo['cantidad']
                productos_controller.edit(producto, None, usuario_id, emprendimiento_id)

    flash('Insumo borrado con éxito!')
    return redirect(url_for('views.insumos_views.insumos'))