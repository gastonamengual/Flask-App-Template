from flask import Blueprint, request, redirect, url_for, flash

from ...controllers import emprendimientos_controller
from ...models.models import Emprendimiento

emprendimientos_scope = Blueprint('emprendimientos_api', __name__, url_prefix='/emprendimientos')

@emprendimientos_scope.post('/emprendimientos')
def emprendimiento_dispatcher():
    data = request.form  
    method = data.get("_method")

    emprendimiento = Emprendimiento(id_ = data.get("id_"),
                                    nombre = data['nombre'],
                                    margen_ganancia=float(data['margen_ganancia']))

    usuario_id = request.cookies.get('usuario_id')

    if method == "POST":
        return emprendimiento_crear(emprendimiento, usuario_id)
    elif method == "PUT":
        return emprendimiento_editar(emprendimiento, usuario_id)
    elif method == "DELETE":
        return emprendimiento_borrar(emprendimiento, usuario_id)
    else:
        raise ValueError("Emprendimiento received an invalid method")

#### CREAR
def emprendimiento_crear(emprendimiento, usuario_id):
    emprendimiento = emprendimientos_controller.create(emprendimiento, usuario_id)
    flash('Emprendimiento creado con éxito!')
    return redirect(url_for('views.emprendimientos_views.emprendimiento_home', id=emprendimiento.id_))

#### EDITAR
def emprendimiento_editar(emprendimiento, usuario_id):
    emprendimiento = emprendimientos_controller.edit(emprendimiento, usuario_id)
    flash('Emprendimiento editado con éxito!')
    return redirect(url_for('views.emprendimientos_views.emprendimiento_home', id=emprendimiento.id_))

#### BORRAR
@emprendimientos_scope.post('/emprendimiento_borrar')
def emprendimiento_borrar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form
    emprendimiento_id = data.get("delete_id")
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    emprendimientos_controller.delete(emprendimiento, usuario_id)

    flash('Emprendimiento borrado con éxito!')
    return redirect(url_for('views.emprendimientos_views.emprendimientos'))