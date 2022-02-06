from ..helpers import pedidos_helper
from ..database import pedidos_db
from ..models.models import Pedido
from typing import List

#### CREAR
def create(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    return pedidos_db.create(pedido, usuario_id, emprendimiento_id)

#### EDITAR
def edit(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    return pedidos_db.update_by_id(pedido, usuario_id, emprendimiento_id)

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Pedido]:
    pedidos = pedidos_db.get_all(usuario_id, emprendimiento_id)
    pedidos_helper.validate_empty_list(pedidos)
    return pedidos

#### GET BY ID
def get_by_id(pedido_: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    pedido = pedidos_db.get_by_id(pedido_, usuario_id, emprendimiento_id)
    return pedido

#### GET BY PROVEEDOR
def get_by_proveedor(usuario_id: int, emprendimiento_id: int, proveedor_id: int) -> List[Pedido]:
    pedidos = pedidos_db.get_all(usuario_id, emprendimiento_id)
    pedidos_proveedor = []
    for pedido in pedidos:
        if pedido.id_proveedor == proveedor_id:
            pedidos_proveedor.append(pedido)
    pedidos_helper.validate_empty_list(pedidos_proveedor)
    return pedidos_proveedor