from typing import List
from ..models.models import Proveedor
from ..models.exceptions import NoEntitiesRegistered

#### VALIDATE EMPTY LIST
def validate_empty_list(proveedores: List[Proveedor]) -> None:
    if proveedores == []:
        raise NoEntitiesRegistered

