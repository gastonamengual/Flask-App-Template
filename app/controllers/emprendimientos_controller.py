from ..helpers import emprendimiento_helper
from ..database import emprendimiento_db
from ..models.models import Emprendimiento
from typing import List

#### REGISTRAR
def create(emprendimiento: Emprendimiento, usuario_id: int) -> Emprendimiento:
    emprendimiento_formateado = emprendimiento_helper.formatear_nombre(emprendimiento)
    emprendimiento_encontrado = emprendimiento_db.get_by_name(emprendimiento_formateado, usuario_id)
    emprendimiento_helper.validate_exists(emprendimiento_encontrado)
    return emprendimiento_db.create(emprendimiento, usuario_id)

### EDITAR
def edit(emprendimiento: Emprendimiento, usuario_id: int) -> Emprendimiento:
    return emprendimiento_db.update_by_id(emprendimiento, usuario_id)

### DELETE
def delete(emprendimiento: Emprendimiento, usuario_id: int):
    emprendimiento_db.delete_by_id(emprendimiento, usuario_id)
    return None

### GET ALL
def get_all(usuario_id) -> List[Emprendimiento]:
    emprendimientos = emprendimiento_db.get_all(usuario_id)
    emprendimiento_helper.validate_empty_list(emprendimientos)
    return emprendimientos

### GET BY ID
def get_by_id(emprendimiento_: Emprendimiento, usuario_id: int) -> Emprendimiento:
    emprendimiento = emprendimiento_db.get_by_id(emprendimiento_, usuario_id)
    return emprendimiento