from dataclasses import asdict
from typing import List, Optional

from ..models.models import Venta, Cliente
from .base_db import db

def get_venta_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Ventas")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_ventas')

#### CREATE PRODUCT
def create(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Venta:
    venta.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_venta_ref(usuario_id, emprendimiento_id).document(venta.id_).set(asdict(venta))
    return venta

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_ventas = doc.to_dict()['num_ventas']
    new_id = str(int(num_ventas) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_ventas': new_id})

    return new_id

#### GET BY ID
def get_by_id(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Optional[Venta]:
    docs = get_venta_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', venta.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        venta_encontrada = Venta(**doc.to_dict())
    return venta_encontrada

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Venta]:

    docs = get_venta_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Venta(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(venta: Venta, usuario_id: int, emprendimiento_id: int) -> Venta:
    get_venta_ref(usuario_id, emprendimiento_id).document(venta.id_).update(asdict(venta))
    return venta

#### GET VENTAS BY PROVEEDOR
def get_ventas_cliente(cliente: Cliente, usuario_id: int, emprendimiento_id: int):
    ventas = get_all(usuario_id, emprendimiento_id)
    ventas_cliente = []
    for venta in ventas:
        if venta.dni_cliente == cliente.dni:
            ventas_cliente.append(venta)
    return ventas_cliente