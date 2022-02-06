from flask import Blueprint, render_template, request, flash, jsonify
from ...controllers import insumos_controller, proveedores_controller, emprendimientos_controller
from ...models.models import Insumo, Emprendimiento
from ...models.exceptions import NoEntitiesRegistered

insumos_scope = Blueprint('insumos_views', __name__, url_prefix='/insumos')

#### INSUMO
@insumos_scope.get("/")
def insumos():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    try:
        insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
        proveedores = []
        for insumo in insumos:
            proveedor = insumos_controller.get_proveedor_name(insumo, usuario_id, emprendimiento_id)
            proveedores.append(proveedor)
            
    except NoEntitiesRegistered:
        insumos = []
        proveedores = []
        flash('Todavía no registraste ningún insumo')
    
    return render_template("emprendimientos/insumos/insumos.html", insumos_proveedores=zip(insumos,proveedores), emprendimiento=emprendimiento)

#### CREAR
@insumos_scope.get("/crear")
def insumo_crear():
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    ### Get all proveedores
    try:
        proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        proveedores = []
        flash('No hay proveedores registrados. Debe registrar alguno.')

    insumo = Insumo()
    
    return render_template("emprendimientos/insumos/insumos_form.html", 
                            method="POST",
                            emprendimiento=emprendimiento, 
                            insumo=insumo,
                            proveedores=proveedores,
                            title='Crear insumo')

#### EDITAR
@insumos_scope.get("/editar/<id>")
def insumo_editar(id):
    insumo_ = Insumo(id_=id)
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)
    
    proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)
    insumo = insumos_controller.get_by_id(insumo_, usuario_id, emprendimiento_id)
    return render_template("emprendimientos/insumos/insumos_form.html", 
                            method="PUT",
                            emprendimiento = emprendimiento,
                            insumo=insumo,
                            proveedores=proveedores,
                            title='Editar insumo')

#### BORRAR (desde ajax)
@insumos_scope.post("/borrar/")
def insumo_borrar():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    
    data = request.form.to_dict()
    insumo_id = (list(data.values()))[0]
    insumo_ = Insumo(id_=insumo_id)
    insumo = insumos_controller.get_by_id(insumo_, usuario_id, emprendimiento_id)

    return jsonify(insumo)