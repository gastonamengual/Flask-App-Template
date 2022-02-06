from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import clientes_controller
from ...models.models import Cliente

clientes_scope = Blueprint('clientes_api', __name__, url_prefix='/clientes')

@clientes_scope.post('/clientes')
def cliente_dispatcher():
    data = request.form
    method = data.get("_method")

    cliente = Cliente(id_ = data.get("id_"),
                      dni = data['dni'],
                      nombre = data['nombre'], 
                      telefono = int(data['telefono']))
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    if method == "POST":
        return cliente_crear(cliente, usuario_id, emprendimiento_id)
    elif method == "PUT":
        return cliente_editar(cliente, usuario_id, emprendimiento_id)
    elif method == "DELETE":
        return cliente_borrar(cliente, usuario_id, emprendimiento_id)
    else:
        raise ValueError("Cliente received an invalid method")

#### CREAR
def cliente_crear(cliente, usuario_id, emprendimiento_id):
    clientes_controller.create(cliente, usuario_id, emprendimiento_id)
    flash('Cliente creado con éxito!')
    return redirect(url_for('views.clientes_views.clientes'))

#### EDITAR
def cliente_editar(cliente, usuario_id, emprendimiento_id):
    clientes_controller.edit(cliente, usuario_id, emprendimiento_id)
    flash('Cliente editado con éxito!')
    return redirect(url_for('views.clientes_views.clientes'))

#### BORRAR
@clientes_scope.post('/cliente_borrar')
def cliente_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    cliente_id = data.get("delete_id")
    cliente_ = Cliente(id_=cliente_id)
    cliente = clientes_controller.get_by_id(cliente_, usuario_id, emprendimiento_id)

    clientes_controller.delete(cliente, usuario_id, emprendimiento_id)

    flash('Cliente borrado con éxito!')
    return redirect(url_for('views.clientes_views.clientes'))