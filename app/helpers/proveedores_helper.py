from typing import List
from dataclasses import asdict
from ..models.models import Proveedor
from ..models.exceptions import EntityExists, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(proveedor: Proveedor) -> Proveedor:
    producto_dict = asdict(proveedor)
    producto_dict["nombre"] = proveedor.nombre.replace(" ", "").lower()

    return Proveedor(**producto_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(proveedor: Proveedor) -> None:
    if proveedor is not None:
        raise EntityExists('El proveedor ya está registrado', 'proveedores', 'producto_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(proveedores: List[Proveedor]) -> None:
    if proveedores == []:
        raise NoEntitiesRegistered

