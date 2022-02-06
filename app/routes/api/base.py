from flask import Blueprint
from .usuarios import usuarios_scope
from .emprendimiento import emprendimientos_scope
from .productos import productos_scope
from .insumos import insumos_scope
from .proveedores import proveedores_scope
from .pedidos import pedidos_scope
from .clientes import clientes_scope
from .costos import costos_scope


api_scope = Blueprint('api', __name__, url_prefix='/api')
api_scope.register_blueprint(usuarios_scope)
api_scope.register_blueprint(emprendimientos_scope)
api_scope.register_blueprint(productos_scope)
api_scope.register_blueprint(insumos_scope)
api_scope.register_blueprint(proveedores_scope)
api_scope.register_blueprint(pedidos_scope)
api_scope.register_blueprint(clientes_scope)
api_scope.register_blueprint(costos_scope)