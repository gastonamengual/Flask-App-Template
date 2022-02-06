from flask import Blueprint, render_template, request, flash, make_response, jsonify
from ...controllers import emprendimientos_controller
from ...models.models import Emprendimiento
from ...models.exceptions import NoEntitiesRegistered

emprendimientos_scope = Blueprint('emprendimientos_views', __name__, url_prefix='/emprendimientos')

#### EMPRENDIMIENTO
@emprendimientos_scope.get("/")
def emprendimientos():
    usuario_id = request.cookies.get('usuario_id')
    try:
        emprendimientos = emprendimientos_controller.get_all(usuario_id)
    except NoEntitiesRegistered:
        emprendimientos = []
        flash('Todavía no registraste ningún emprendimiento')
    
    return render_template("emprendimientos/emprendimientos.html", emprendimientos=emprendimientos)

#### EMPRENDIMIENTO HOME
@emprendimientos_scope.get("/emprendimiento_home/<id>")
def emprendimiento_home(id):
    emprendimiento_ = Emprendimiento(id_=id)
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)
    
    resp = make_response(render_template("/emprendimientos/emprendimiento_home.html", method="POST", emprendimiento=emprendimiento))
    resp.set_cookie('emprendimiento_id', emprendimiento.id_)
   
    return resp

#### EDITAR (desde ajax)
@emprendimientos_scope.post("/editar/")
def emprendimiento_editar():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    emprendimiento_id = (list(data.values()))[0]
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    return jsonify(emprendimiento)

#### BORRAR (desde ajax)
@emprendimientos_scope.post("/borrar/")
def emprendimiento_borrar():
    usuario_id = request.cookies.get('usuario_id')
    
    data = request.form.to_dict()
    emprendimiento_id = (list(data.values()))[0]
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    return jsonify(emprendimiento)