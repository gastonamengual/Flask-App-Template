from flask import Blueprint, render_template, request, flash, jsonify
from ...controllers import clientes_controller, emprendimientos_controller
from ...models.models import Cliente, Emprendimiento
from ...models.exceptions import NoEntitiesRegistered

clientes_scope = Blueprint('clientes_views', __name__, url_prefix='/clientes')

#### CLIENTE
@clientes_scope.get("/")
def clientes():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    try:
        clientes = clientes_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        clientes = []
        flash('Todavía no registraste ningún cliente')
    
    return render_template("emprendimientos/clientes/clientes.html", clientes=clientes, emprendimiento=emprendimiento)

#### EDITAR (desde ajax)
@clientes_scope.post("/editar/")
def cliente_editar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    cliente_id = (list(data.values()))[0]
    cliente_ = Cliente(id_=cliente_id)
    cliente = clientes_controller.get_by_id(cliente_, usuario_id, emprendimiento_id)

    return jsonify(cliente)

#### BORRAR (desde ajax)
@clientes_scope.post("/borrar/")
def cliente_borrar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    data = request.form.to_dict()
    cliente_id = (list(data.values()))[0]
    cliente_ = Cliente(id_=cliente_id)
    cliente = clientes_controller.get_by_id(cliente_, usuario_id, emprendimiento_id)

    return jsonify(cliente)