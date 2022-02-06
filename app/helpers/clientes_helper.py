from typing import List
from dataclasses import asdict
from ..models.models import Cliente
from ..models.exceptions import EntityExists, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(cliente: Cliente) -> Cliente:
    producto_dict = asdict(cliente)
    producto_dict["nombre"] = cliente.nombre.replace(" ", "").lower()

    return Cliente(**producto_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(cliente: Cliente) -> None:
    if cliente is not None:
        raise EntityExists('El cliente ya está registrado', 'clientes', 'producto_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(clientes: List[Cliente]) -> None:
    if clientes == []:
        raise NoEntitiesRegistered

