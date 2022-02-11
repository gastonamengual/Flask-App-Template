from typing import List
from dataclasses import asdict
from ..models.models import Producto
from ..models.exceptions import EntityExists, NoEntitiesRegistered, NoEntitiesRegistered

#### FORMATEAR NOMBRE
def formatear_nombre(nombre: str) -> Producto:
    return nombre.replace(" ", "").lower()

#### VALIDATE PRODUCTO EXISTS
def validate_exists(producto: Producto, productos: List[Producto]) -> None:
    nombre_formateado = formatear_nombre(producto.nombre)
    for producto in productos:
        if formatear_nombre(producto.nombre) == nombre_formateado:
            raise EntityExists('El producto ya está registrado', 'productos_views', 'producto_crear')

#### VALIDATE EMPTY LIST
def validate_empty_list(productos: List[Producto]) -> None:
    if productos == []:
        raise NoEntitiesRegistered

