from ..helpers import proveedores_helper
from ..database import proveedores_db
from ..models.models import Proveedor
from typing import List

from ..controllers import productos_controller, insumos_controller

#### CREAR
def create(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    proveedor_formateado = proveedores_helper.formatear_nombre(proveedor)
    proveedor_encontrado = proveedores_db.get_by_name(proveedor_formateado, usuario_id, emprendimiento_id)
    proveedores_helper.validate_exists(proveedor_encontrado)
    return proveedores_db.create(proveedor, usuario_id, emprendimiento_id)

#### EDITAR
def edit(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    return proveedores_db.update_by_id(proveedor, usuario_id, emprendimiento_id)

#### DELETE
def delete(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int):
    proveedores_db.delete_by_id(proveedor, usuario_id, emprendimiento_id)
    return None

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Proveedor]:
    proveedores = proveedores_db.get_all(usuario_id, emprendimiento_id)
    proveedores_helper.validate_empty_list(proveedores)
    return proveedores

#### GET BY ID
def get_by_id(proveedor_: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    proveedor = proveedores_db.get_by_id(proveedor_, usuario_id, emprendimiento_id)
    return proveedor

#### GET ARTICULOS
def get_articulos(proveedor: Proveedor, usuario_id: int , emprendimiento_id: int):
    productos = productos_controller.get_productos_proveedor(proveedor, usuario_id, emprendimiento_id)
    insumos = insumos_controller.get_insumos_proveedor(proveedor, usuario_id, emprendimiento_id)
    articulos = productos + insumos
    proveedores_helper.validate_empty_list(articulos)
    return articulos