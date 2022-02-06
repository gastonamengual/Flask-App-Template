from ..helpers import costos_helper
from ..database import costos_db
from ..models.models import Costo
from typing import List

#### CREAR
def create(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    costo_formateado = costos_helper.formatear_nombre(costo)
    costo_encontrado = costos_db.get_by_name(costo_formateado, usuario_id, emprendimiento_id)
    costos_helper.validate_exists(costo_encontrado)
    return costos_db.create(costo, usuario_id, emprendimiento_id)

#### EDITAR
def edit(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    return costos_db.update_by_id(costo, usuario_id, emprendimiento_id)

#### DELETE
def delete(costo: Costo, usuario_id: int, emprendimiento_id: int):
    costos_db.delete_by_id(costo, usuario_id, emprendimiento_id)
    return None

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Costo]:
    costos = costos_db.get_all(usuario_id, emprendimiento_id)
    costos_helper.validate_empty_list(costos)
    return costos

#### GET BY ID
def get_by_id(costo_: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    costo = costos_db.get_by_id(costo_, usuario_id, emprendimiento_id)
    return costo