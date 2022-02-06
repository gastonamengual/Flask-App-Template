from dataclasses import asdict
from typing import List, Optional

from ..models.models import Proveedor
from .base_db import db

def get_proveedor_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Proveedores")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_proveedores')

#### CREATE PRODUCT
def create(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    proveedor.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_proveedor_ref(usuario_id, emprendimiento_id).document(proveedor.id_).set(asdict(proveedor))
    return proveedor

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_proveedores = doc.to_dict()['num_proveedores']
    new_id = str(int(num_proveedores) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_proveedores': new_id})

    return new_id

#### GET BY ID
def get_by_id(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Optional[Proveedor]:
    docs = get_proveedor_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', proveedor.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        proveedor_encontrado = Proveedor(**doc.to_dict())
    return proveedor_encontrado

#### GET BY NAME
def get_by_name(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    docs = get_proveedor_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', proveedor.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        proveedor_encontrado = Proveedor(**doc.to_dict())
    return proveedor_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Proveedor]:

    docs = get_proveedor_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Proveedor(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> Proveedor:
    get_proveedor_ref(usuario_id, emprendimiento_id).document(proveedor.id_).update(asdict(proveedor))
    return proveedor

#### DELETE ENTITY BY ID
def delete_by_id(proveedor: Proveedor, usuario_id: int, emprendimiento_id: int) -> None:
    get_proveedor_ref(usuario_id, emprendimiento_id).document(proveedor.id_).delete()