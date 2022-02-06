from dataclasses import asdict
from typing import List, Optional

from ..models.models import Usuario
from .base_db import db

usuario_ref = db.collection(u"Usuarios")

#### CREATE
def create(usuario: Usuario) -> Usuario:
    usuario.id_ = autoincrement_id()
    usuario_ref.document(usuario.id_).set(asdict(usuario))
    return usuario

#### AUTOINCREMENTAL ID
def autoincrement_id() -> int:
    usuarios = get_all()
    if usuarios == []:
        return "0"

    last_id = max(usuarios, key=lambda x: int(x.id_)).id_
    new_id = str(int(last_id) + 1)
    return new_id

#### GET BY EMAIL
def get_by_email(usuario: Usuario) -> Usuario:
    docs = usuario_ref.where(u'email', u'==', usuario.email).get()
    if docs == []:
        return None
    
    for doc in docs:
        usuario_encontrado = Usuario(**doc.to_dict())
    return usuario_encontrado

#### GET ALL
def get_all() -> List[Usuario]:

    docs = usuario_ref.get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Usuario(**doc.to_dict()))
    
    return results

#### GET BY ID
def get_by_id(usuario: Usuario) -> Optional[Usuario]:
    docs = usuario_ref.where(u'id_', u'==', usuario.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        usuario_encontrado = Usuario(**doc.to_dict())
    return usuario_encontrado

#### UPDATE BY ID
def update_by_id(usuario: Usuario) -> Usuario:
    usuario_ref.document(usuario.id_).update(asdict(usuario))
    return usuario

#### DELETE ENTITY BY ID
def delete_by_id(usuario: Usuario) -> None:
    usuario_ref.document(usuario.id_).delete()