from ..helpers import insumos_helper
from ..database import insumos_db
from ..models.models import Insumo, Proveedor
from typing import List

from ..controllers import proveedores_controller 

#### CREAR
def create(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    insumo_formateado = insumos_helper.formatear_nombre(insumo)
    insumo_encontrado = insumos_db.get_by_name(insumo_formateado, usuario_id, emprendimiento_id)
    insumos_helper.validate_exists(insumo_encontrado)
    return insumos_db.create(insumo, usuario_id, emprendimiento_id)

#### EDITAR
def edit(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    return insumos_db.update_by_id(insumo, usuario_id, emprendimiento_id)

#### DELETE
def delete(insumo: Insumo, usuario_id: int, emprendimiento_id: int):
    insumos_db.delete_by_id(insumo, usuario_id, emprendimiento_id)
    return None

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Insumo]:
    insumos = insumos_db.get_all(usuario_id, emprendimiento_id)
    insumos_helper.validate_empty_list(insumos)
    return insumos

#### GET BY ID
def get_by_id(insumo_: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    insumo = insumos_db.get_by_id(insumo_, usuario_id, emprendimiento_id)
    return insumo

#### GET INSUMOS PROVEEDOR
def get_insumos_proveedor(proveedor, usuario_id, emprendimiento_id):
    insumos = insumos_db.get_insumos_by_proveedor(proveedor, usuario_id, emprendimiento_id)
    return insumos

### GET PROVEEDOR NAME
def get_proveedor_name(insumo: Insumo, usuario_id:int, emprendimiento_id:int):
    proveedor = Proveedor(id_=insumo.id_proveedor)
    proveedor_encontrado = proveedores_controller.get_by_id(proveedor, usuario_id, emprendimiento_id)
    return proveedor_encontrado