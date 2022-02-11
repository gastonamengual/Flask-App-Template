from datetime import datetime

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from ...controllers import costos_controller, emprendimientos_controller
from ...models.models import Costo, Emprendimiento
from ...models.exceptions import NoEntitiesRegistered

costos_scope = Blueprint('costos_views', __name__, url_prefix='/costos')

#### CLIENTE
@costos_scope.get("/")
def costos():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    try:
        costos = costos_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        costos = []
        flash('Todavía no registraste ningún costo')
    
    return render_template("emprendimientos/costos/costos.html", costos=costos, emprendimiento=emprendimiento)

#### EDITAR (desde ajax)
@costos_scope.post("/editar/")
def costo_editar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    costo_id = (list(data.values()))[0]
    costo_ = Costo(id_=costo_id)
    costo = costos_controller.get_by_id(costo_, usuario_id, emprendimiento_id)

    return jsonify(costo)

#### BORRAR (desde ajax)
@costos_scope.post("/borrar/")
def costo_borrar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    data = request.form.to_dict()
    costo_id = (list(data.values()))[0]
    costo_ = Costo(id_=costo_id)
    costo = costos_controller.get_by_id(costo_, usuario_id, emprendimiento_id)

    return jsonify(costo)

#### LISTA PAGOS
@costos_scope.get("/lista_pagos/<costo_id>")
def lista_pagos(costo_id):

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get costo
    costo_ = Costo(id_=costo_id)
    costo = costos_controller.get_by_id(costo_, usuario_id, emprendimiento_id)
    
    for pago in costo.pagos:
        pago['fecha'] = datetime.strptime(pago['fecha'], '%Y-%m-%d').strftime('%d/%m/%Y')


    return render_template("emprendimientos/costos/lista_pagos.html",
                           costo=costo,
                           pagos=costo.pagos,
                           emprendimiento=emprendimiento)