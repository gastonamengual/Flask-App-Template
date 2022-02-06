from typing import List
from dataclasses import asdict
from ..models.models import Costo
from ..models.exceptions import EntityExists, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(costo: Costo) -> Costo:
    producto_dict = asdict(costo)
    producto_dict["nombre"] = costo.nombre.replace(" ", "").lower()

    return Costo(**producto_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(costo: Costo) -> None:
    if costo is not None:
        raise EntityExists('El costo ya está registrado', 'costos', 'producto_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(costos: List[Costo]) -> None:
    if costos == []:
        raise NoEntitiesRegistered

