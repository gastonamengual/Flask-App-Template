from flask import Blueprint
from .usuarios import usuarios_scope
from .emprendimiento import emprendimientos_scope
from .productos import productos_scope
from .insumos import insumos_scope
from .proveedores import proveedores_scope
from .pedidos import pedidos_scope
from .clientes import clientes_scope
from .ventas import ventas_scope
from .informes import informe_scope
from .informe_ventas import informe_ventas_scope
from .informe_productos import informe_productos_scope
from .informe_clientes import informe_clientes_scope
from .informe_proveedores import informe_proveedores_scope
from .costos import costos_scope


views_scope = Blueprint('views', __name__, url_prefix='/')
views_scope.register_blueprint(usuarios_scope)
views_scope.register_blueprint(emprendimientos_scope)
views_scope.register_blueprint(productos_scope)
views_scope.register_blueprint(insumos_scope)
views_scope.register_blueprint(proveedores_scope)
views_scope.register_blueprint(pedidos_scope)
views_scope.register_blueprint(clientes_scope)
views_scope.register_blueprint(ventas_scope)
views_scope.register_blueprint(informe_scope)
views_scope.register_blueprint(informe_ventas_scope)
views_scope.register_blueprint(informe_productos_scope)
views_scope.register_blueprint(informe_clientes_scope)
views_scope.register_blueprint(informe_proveedores_scope)
views_scope.register_blueprint(costos_scope)