from typing import List
from dataclasses import asdict
from ..models.models import Producto
from ..models.exceptions import EntityExists, NoEntitiesRegistered, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(producto: Producto) -> Producto:
    producto_dict = asdict(producto)
    producto_dict["nombre"] = producto.nombre.replace(" ", "").lower()

    return Producto(**producto_dict)

#### VALIDATE EMPRENDIMIENTO EXISTS
def validate_exists(producto: Producto) -> None:
    if producto is not None:
        raise EntityExists('El producto ya está registrado', 'productos', 'producto_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(productos: List[Producto]) -> None:
    if productos == []:
        raise NoEntitiesRegistered

