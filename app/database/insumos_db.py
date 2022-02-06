from dataclasses import asdict
from typing import List, Optional

from ..models.models import Insumo
from .base_db import db

def get_insumo_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Insumos")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_articulos')

#### CREATE
def create(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    insumo.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_insumo_ref(usuario_id, emprendimiento_id).document(insumo.id_).set(asdict(insumo))
    return insumo

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_articulos = doc.to_dict()['num_articulos']
    new_id = str(int(num_articulos) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_articulos': new_id})

    return new_id

#### GET BY ID
def get_by_id(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Optional[Insumo]:
    docs = get_insumo_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', insumo.id_).get()
    if docs == []:
        return None
    
    for doc in docs:
        insumo_encontrado = Insumo(**doc.to_dict())
    return insumo_encontrado

#### GET BY NAME
def get_by_name(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    docs = get_insumo_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', insumo.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        insumo_encontrado = Insumo(**doc.to_dict())
    return insumo_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Insumo]:

    docs = get_insumo_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Insumo(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> Insumo:
    get_insumo_ref(usuario_id, emprendimiento_id).document(insumo.id_).update(asdict(insumo))
    return insumo

#### DELETE ENTITY BY ID
def delete_by_id(insumo: Insumo, usuario_id: int, emprendimiento_id: int) -> None:
    get_insumo_ref(usuario_id, emprendimiento_id).document(insumo.id_).delete()

#### GET INSUMOS BY PROVEEDOR
def get_insumos_by_proveedor(proveedor, usuario_id, emprendimiento_id):
    insumos = get_all(usuario_id, emprendimiento_id)
    insumos_proveedor = []
    for insumo in insumos:
        if insumo.id_proveedor == proveedor.id_:
            insumos_proveedor.append(insumo)
    return insumos_proveedor