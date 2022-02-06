from flask import Blueprint, render_template, request
from ...controllers import productos_controller, emprendimientos_controller, clientes_controller, proveedores_controller
from ...models.models import Emprendimiento

informe_scope = Blueprint('informes_views', __name__, url_prefix='/informes')

#### INFORMES
@informe_scope.get("/")
def informes():
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    productos = productos_controller.get_all(usuario_id, emprendimiento_id)
    clientes = clientes_controller.get_all(usuario_id, emprendimiento_id)
    proveedores = proveedores_controller.get_all(usuario_id, emprendimiento_id)

    return render_template("emprendimientos/informes/informes.html", 
                            emprendimiento=emprendimiento,
                            productos=productos,
                            clientes=clientes,
                            proveedores=proveedores)