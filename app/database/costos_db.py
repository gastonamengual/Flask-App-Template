from dataclasses import asdict
from typing import List, Optional

from ..models.models import Costo
from .base_db import db

def get_costo_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Costos")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_costos')

#### CREATE PRODUCT
def create(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    costo.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_costo_ref(usuario_id, emprendimiento_id).document(costo.id_).set(asdict(costo))
    return costo

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_costos = doc.to_dict()['num_costos']
    new_id = str(int(num_costos) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_costos': new_id})

    return new_id

#### GET BY ID
def get_by_id(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Optional[Costo]:
    docs = get_costo_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', costo.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        costo_encontrado = Costo(**doc.to_dict())
    return costo_encontrado

#### GET BY NAME
def get_by_name(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    docs = get_costo_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', costo.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        costo_encontrado = Costo(**doc.to_dict())
    return costo_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Costo]:

    docs = get_costo_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Costo(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(costo: Costo, usuario_id: int, emprendimiento_id: int) -> Costo:
    get_costo_ref(usuario_id, emprendimiento_id).document(costo.id_).update(asdict(costo))
    return costo

#### DELETE ENTITY BY ID
def delete_by_id(costo: Costo, usuario_id: int, emprendimiento_id: int) -> None:
    get_costo_ref(usuario_id, emprendimiento_id).document(costo.id_).delete()