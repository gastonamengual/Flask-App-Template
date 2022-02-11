from typing import List
from dataclasses import asdict
from ..models.models import Insumo
from ..models.exceptions import EntityExists, NoEntitiesRegistered, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(nombre: str) -> Insumo:
    return nombre.replace(" ", "").lower()

#### VALIDATE PRODUCTO EXISTS
def validate_exists(insumo: Insumo, insumos: List[Insumo]) -> None:
    nombre_formateado = formatear_nombre(insumo.nombre)
    for insumo in insumos:
        if formatear_nombre(insumo.nombre) == nombre_formateado:
            raise EntityExists('El insumo ya está registrado', 'insumos_views', 'insumo_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(insumos: List[Insumo]) -> None:
    if insumos == []:
        raise NoEntitiesRegistered

