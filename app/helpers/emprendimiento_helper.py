from typing import List
from dataclasses import asdict
from ..models.models import Emprendimiento
from ..models.exceptions import EntityExists, NoEntitiesRegistered, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(emprendimiento: Emprendimiento) -> Emprendimiento:
    emprendimiento_dict = asdict(emprendimiento)
    emprendimiento_dict["nombre"] = emprendimiento.nombre.replace(" ", "").lower()

    return Emprendimiento(**emprendimiento_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(emprendimiento: Emprendimiento) -> None:
    if emprendimiento is not None:
        raise EntityExists('El emprendimiento ya está registrado', 'emprendimientos', 'emprendimiento_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(emprendimientos: List[Emprendimiento]) -> None:
    if emprendimientos == []:
        raise NoEntitiesRegistered