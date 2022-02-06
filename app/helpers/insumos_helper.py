from typing import List
from dataclasses import asdict
from ..models.models import Insumo
from ..models.exceptions import EntityExists, NoEntitiesRegistered, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(insumo: Insumo) -> Insumo:
    insumo_dict = asdict(insumo)
    insumo_dict["nombre"] = insumo.nombre.replace(" ", "").lower()

    return Insumo(**insumo_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(insumo: Insumo) -> None:
    if insumo is not None:
        raise EntityExists('El insumo ya está registrado', 'insumos', 'insumo_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(insumos: List[Insumo]) -> None:
    if insumos == []:
        raise NoEntitiesRegistered

