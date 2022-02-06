from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import proveedores_controller
from ...models.models import Proveedor

proveedores_scope = Blueprint('proveedores_api', __name__, url_prefix='/proveedores')

@proveedores_scope.post('/proveedores')
def proveedor_dispatcher():
    data = request.form
    method = data.get("_method")

    proveedor = Proveedor(id_ = data.get("id_"),
                          nombre = data['nombre'], 
                          telefono = data['telefono'])
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    if method == "POST":
        return proveedor_crear(proveedor, usuario_id, emprendimiento_id)
    elif method == "PUT":
        return proveedor_editar(proveedor, usuario_id, emprendimiento_id)
    elif method == "DELETE":
        return proveedor_borrar(proveedor, usuario_id, emprendimiento_id)
    else:
        raise ValueError("Proveedor received an invalid method")

#### CREAR
def proveedor_crear(proveedor, usuario_id, emprendimiento_id):
    proveedores_controller.create(proveedor, usuario_id, emprendimiento_id)
    flash('Proveedor creado con éxito!')
    return redirect(url_for('views.proveedores_views.proveedores'))

#### EDITAR
def proveedor_editar(proveedor, usuario_id, emprendimiento_id):
    proveedores_controller.edit(proveedor, usuario_id, emprendimiento_id)
    flash('Proveedor editado con éxito!')
    return redirect(url_for('views.proveedores_views.proveedores'))

#### BORRAR
@proveedores_scope.post('/proveedor_borrar')
def proveedor_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    proveedor_id = data.get("delete_id")
    proveedor_ = Proveedor(id_=proveedor_id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)

    proveedores_controller.delete(proveedor, usuario_id, emprendimiento_id)

    flash('Proveedor borrado con éxito!')
    return redirect(url_for('views.proveedores_views.proveedores'))