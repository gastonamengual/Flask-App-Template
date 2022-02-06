from ..helpers import ventas_helper
from ..database import ventas_db
from ..models.models import Venta, Cliente
from typing import List

#### CREAR
def create(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Venta:
    return ventas_db.create(venta, usuario_id, emprendimiento_id)

#### EDITAR
def edit(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Venta:
    return ventas_db.update_by_id(venta, usuario_id, emprendimiento_id)

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Venta]:
    pedidos = ventas_db.get_all(usuario_id, emprendimiento_id)
    ventas_helper.validate_empty_list(pedidos)
    return pedidos

#### GET BY ID
def get_by_id(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Venta:
    venta = ventas_db.get_by_id(venta, usuario_id, emprendimiento_id)
    return venta

#### GET VENTAS CLIENTE
def get_ventas_cliente(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> List[Venta]:
    ventas_cliente = ventas_db.get_ventas_cliente(cliente, usuario_id, emprendimiento_id)
    return ventas_cliente