from datetime import datetime

from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import costos_controller
from ...models.models import Costo, CostoPago

costos_scope = Blueprint('costos_api', __name__, url_prefix='/costos')

@costos_scope.post('/costos')
def costo_dispatcher():
    data = request.form
    method = data.get("_method")

    costo = Costo(id_ = data.get("id_"),
                  nombre = data['nombre'],
                  frecuencia_pago = float(data['frecuencia_pago']),
                  pagos=[])
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    if method == "POST":
        return costo_crear(costo, usuario_id, emprendimiento_id)
    elif method == "PUT":
        return costo_editar(costo, usuario_id, emprendimiento_id)
    elif method == "DELETE":
        return costo_borrar(costo, usuario_id, emprendimiento_id)
    else:
        raise ValueError("Costo received an invalid method")

#### CREAR
def costo_crear(costo, usuario_id, emprendimiento_id):
    costos_controller.create(costo, usuario_id, emprendimiento_id)
    flash('Costo creado con éxito!')
    return redirect(url_for('views.costos_views.costos'))

#### EDITAR
def costo_editar(costo, usuario_id, emprendimiento_id):
    costos_controller.edit(costo, usuario_id, emprendimiento_id)
    flash('Costo editado con éxito!')
    return redirect(url_for('views.costos_views.costos'))

#### BORRAR
@costos_scope.post('/costo_borrar')
def costo_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    costo_id = data.get("delete_id")
    costo_ = Costo(id_=costo_id)
    costo = costos_controller.get_by_id(costo_, usuario_id, emprendimiento_id)

    costos_controller.delete(costo, usuario_id, emprendimiento_id)

    flash('Costo borrado con éxito!')
    return redirect(url_for('views.costos_views.costos'))

#### CREAR PAGO
@costos_scope.post('/agregar_pago')
def agregar_pago():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    costo_id = data.get("id_")
    importe = data['importe']

    ### Get costo
    costo_ = Costo(id_=costo_id)
    costo = costos_controller.get_by_id(costo_, usuario_id, emprendimiento_id)
    
    pago = CostoPago(fecha=datetime.today(), importe=float(importe))
    costo.pagos.append(pago)

    costos_controller.edit(costo, usuario_id, emprendimiento_id)
    flash('Pago registrado con éxito!')
    return redirect(url_for('views.costos_views.lista_pagos', costo_id=costo.id_))