from dataclasses import asdict
from typing import List, Optional

from ..models.models import Pedido
from .base_db import db

def get_pedido_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Pedidos")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_pedidos')

#### CREATE PRODUCT
def create(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    pedido.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_pedido_ref(usuario_id, emprendimiento_id).document(pedido.id_).set(asdict(pedido))
    return pedido

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_pedidos = doc.to_dict()['num_pedidos']
    new_id = str(int(num_pedidos) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_pedidos': new_id})

    return new_id

#### GET BY ID
def get_by_id(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Optional[Pedido]:
    docs = get_pedido_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', pedido.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        pedido_encontrado = Pedido(**doc.to_dict())
    return pedido_encontrado

#### GET BY NAME
def get_by_name(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    docs = get_pedido_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', pedido.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        pedido_encontrado = Pedido(**doc.to_dict())
    return pedido_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Pedido]:

    docs = get_pedido_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Pedido(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> Pedido:
    get_pedido_ref(usuario_id, emprendimiento_id).document(pedido.id_).update(asdict(pedido))
    return pedido

#### DELETE ENTITY BY ID
def delete_by_id(pedido: Pedido, usuario_id: int, emprendimiento_id: int) -> None:
    get_pedido_ref(usuario_id, emprendimiento_id).document(pedido.id_).delete()