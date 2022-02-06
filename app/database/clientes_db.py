from dataclasses import asdict
from typing import List, Optional

from ..models.models import Cliente
from .base_db import db

def get_cliente_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Clientes")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_clientes')

#### CREATE PRODUCT
def create(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    cliente.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_cliente_ref(usuario_id, emprendimiento_id).document(cliente.id_).set(asdict(cliente))
    return cliente

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_clientes = doc.to_dict()['num_clientes']
    new_id = str(int(num_clientes) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_clientes': new_id})

    return new_id

#### GET BY ID
def get_by_id(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Optional[Cliente]:
    docs = get_cliente_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', cliente.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        cliente_encontrado = Cliente(**doc.to_dict())
    return cliente_encontrado

#### GET BY DNI
def get_by_dni(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Optional[Cliente]:
    docs = get_cliente_ref(usuario_id, emprendimiento_id).where(u'dni', u'==', cliente.dni).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        cliente_encontrado = Cliente(**doc.to_dict())
    return cliente_encontrado

#### GET BY NAME
def get_by_name(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    docs = get_cliente_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', cliente.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        cliente_encontrado = Cliente(**doc.to_dict())
    return cliente_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Cliente]:

    docs = get_cliente_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Cliente(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> Cliente:
    get_cliente_ref(usuario_id, emprendimiento_id).document(cliente.id_).update(asdict(cliente))
    return cliente

#### DELETE ENTITY BY ID
def delete_by_id(cliente: Cliente, usuario_id: int, emprendimiento_id: int) -> None:
    get_cliente_ref(usuario_id, emprendimiento_id).document(cliente.id_).delete()