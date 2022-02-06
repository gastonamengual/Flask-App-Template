from typing import List
from ..models.models import Venta
from ..models.exceptions import NoEntitiesRegistered

#### VALIDATE EMPTY LIST
def validate_empty_list(ventas: List[Venta]) -> None:
    if ventas == []:
        raise NoEntitiesRegistered

