from ..helpers import clientes_helper
from ..database import clientes_db
from ..models.models import Cliente
from typing import List

from ..controllers import ventas_controller

#### CREAR
def create(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    cliente_formateado = clientes_helper.formatear_nombre(cliente)
    cliente_encontrado = clientes_db.get_by_name(cliente_formateado, usuario_id, emprendimiento_id)
    clientes_helper.validate_exists(cliente_encontrado)
    return clientes_db.create(cliente, usuario_id, emprendimiento_id)

#### EDITAR
def edit(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    return clientes_db.update_by_id(cliente, usuario_id, emprendimiento_id)

#### DELETE
def delete(cliente: Cliente, usuario_id: int, emprendimiento_id: int):
    clientes_db.delete_by_id(cliente, usuario_id, emprendimiento_id)
    return None

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Cliente]:
    clientes = clientes_db.get_all(usuario_id, emprendimiento_id)
    clientes_helper.validate_empty_list(clientes)
    return clientes

#### GET BY ID
def get_by_id(cliente_: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    cliente = clientes_db.get_by_id(cliente_, usuario_id, emprendimiento_id)
    return cliente

#### GET BY DNI
def get_by_dni(cliente_: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    cliente = clientes_db.get_by_dni(cliente_, usuario_id, emprendimiento_id)
    return cliente

#### GET PRODUCTS
def get_ventas(cliente: Cliente, usuario_id: int , emprendimiento_id: int):
    ventas = ventas_controller.get_ventas_cliente(cliente, usuario_id, emprendimiento_id)
    clientes_helper.validate_empty_list(ventas)
    return ventas