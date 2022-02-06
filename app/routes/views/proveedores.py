from flask import Blueprint, render_template, request, flash, jsonify
from ...controllers import proveedores_controller, emprendimientos_controller
from ...models.models import Proveedor, Emprendimiento
from ...models.exceptions import NoEntitiesRegistered

proveedores_scope = Blueprint('proveedores_views', __name__, url_prefix='/proveedores')

#### PROVEEDOR
@proveedores_scope.get("/")
def proveedores():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    try:
        proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        proveedores = []
        flash('Todavía no registraste ningún proveedor')
    
    return render_template("emprendimientos/proveedores/proveedores.html", proveedores=proveedores, emprendimiento=emprendimiento)

#### EDITAR (desde ajax)
@proveedores_scope.post("/editar/")
def proveedor_editar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')

    data = request.form.to_dict()
    proveedor_id = (list(data.values()))[0]
    proveedor_ = Proveedor(id_=proveedor_id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)

    return jsonify(proveedor)

#### BORRAR (desde ajax)
@proveedores_scope.post("/borrar/")
def proveedor_borrar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    data = request.form.to_dict()
    proveedor_id = (list(data.values()))[0]
    proveedor_ = Proveedor(id_=proveedor_id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)

    return jsonify(proveedor)

#### LISTA PRODUCTOS
@proveedores_scope.get("/lista_productos/<id>")
def lista_productos(id):

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    proveedor_ = Proveedor(id_=id)
    proveedor = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)

    try:
        articulos = proveedores_controller.get_articulos(proveedor, usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        flash('Todavía no registraste ningún producto o insumo para este proveedor')
        return proveedores()
    
    return render_template("emprendimientos/proveedores/lista_productos.html", 
                            emprendimiento=emprendimiento,
                            articulos=articulos,
                            proveedor=proveedor)