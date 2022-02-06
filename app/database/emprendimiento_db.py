from dataclasses import asdict
from typing import List, Optional

from ..models.models import Emprendimiento
from .base_db import db

def get_emprendimiento_ref(usuario_id):
    return db.collection(u"Usuarios").document(usuario_id).collection("Emprendimientos")

def create_global_nums(usuario_id: int, emprendimiento_id: int):
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_clientes').set({'num_clientes': "-1"})
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_costos').set({'num_costos': "-1"})
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_articulos').set({'num_articulos': "-1"})
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_pedidos').set({'num_pedidos': "-1"})
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_proveedores').set({'num_proveedores': "-1"})
    db.collection(u"Usuarios").document(usuario_id).collection(u"Emprendimientos").document(emprendimiento_id).collection("Global").document('num_ventas').set({'num_ventas': "-1"})

#### CREATE
def create(emprendimiento: Emprendimiento, usuario_id: int) -> Emprendimiento:
    emprendimiento.id_ = autoincrement_id(usuario_id)
    get_emprendimiento_ref(usuario_id).document(emprendimiento.id_).set(asdict(emprendimiento))
    create_global_nums(usuario_id, emprendimiento.id_)
    return emprendimiento

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int) -> int:
    emprendimientos = get_all(usuario_id)
    if emprendimientos == []:
        return "0"

    last_id = max(emprendimientos, key=lambda x: int(x.id_)).id_
    new_id = str(int(last_id) + 1)
    return new_id

### GET BY ID
def get_by_id(emprendimiento: Emprendimiento, usuario_id: int) -> Optional[Emprendimiento]:
    docs = get_emprendimiento_ref(usuario_id).where(u'id_', u'==', emprendimiento.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        emprendimiento_encontrado = Emprendimiento(**doc.to_dict())
    return emprendimiento_encontrado

#### GET BY NAME
def get_by_name(emprendimiento: Emprendimiento, usuario_id: int) -> Emprendimiento:
    docs = get_emprendimiento_ref(usuario_id).where(u'nombre', u'==', emprendimiento.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        emprendimiento_encontrado = Emprendimiento(**doc.to_dict())
    return emprendimiento_encontrado

#### GET ALL
def get_all(usuario_id: int) -> List[Emprendimiento]:

    docs = get_emprendimiento_ref(usuario_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Emprendimiento(**doc.to_dict()))
    
    return results

### UPDATE BY ID
def update_by_id(emprendimiento: Emprendimiento, usuario_id: int) -> Emprendimiento:
    get_emprendimiento_ref(usuario_id).document(emprendimiento.id_).update(asdict(emprendimiento))
    return emprendimiento

### DELETE ENTITY BY ID
def delete_by_id(emprendimiento: Emprendimiento, usuario_id: int) -> None:
    get_emprendimiento_ref(usuario_id).document(emprendimiento.id_).delete()