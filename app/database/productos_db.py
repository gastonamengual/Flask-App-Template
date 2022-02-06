from dataclasses import asdict
from typing import List, Optional

from ..models.models import Producto
from .base_db import db

def get_producto_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Productos")

def get_global_ref(usuario_id, emprendimiento_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection("Global").document('num_articulos')

#### CREATE
def create(producto: Producto, usuario_id: int, emprendimiento_id: int) -> Producto:
    producto.id_ = autoincrement_id(usuario_id, emprendimiento_id)
    get_producto_ref(usuario_id, emprendimiento_id).document(producto.id_).set(asdict(producto))
    return producto

#### AUTOINCREMENTAL ID
def autoincrement_id(usuario_id: int, emprendimiento_id: int) -> int:
    
    doc = get_global_ref(usuario_id, emprendimiento_id).get()
    num_articulos = doc.to_dict()['num_articulos']
    new_id = str(int(num_articulos) + 1)
    get_global_ref(usuario_id, emprendimiento_id).set({'num_articulos': new_id})

    return new_id

#### GET BY ID
def get_by_id(producto: Producto, usuario_id: int, emprendimiento_id: int) -> Optional[Producto]:
    docs = get_producto_ref(usuario_id, emprendimiento_id).where(u'id_', u'==', producto.id_).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        producto_encontrado = Producto(**doc.to_dict())
    return producto_encontrado

#### GET BY NAME
def get_by_name(producto: Producto, usuario_id: int, emprendimiento_id: int) -> Producto:
    docs = get_producto_ref(usuario_id, emprendimiento_id).where(u'nombre', u'==', producto.nombre).get()
    
    if docs == []:
        return None
    
    for doc in docs:
        producto_encontrado = Producto(**doc.to_dict())
    return producto_encontrado

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Producto]:

    docs = get_producto_ref(usuario_id, emprendimiento_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(Producto(**doc.to_dict()))
    
    return results

#### UPDATE BY ID
def update_by_id(producto: Producto, usuario_id: int, emprendimiento_id: int) -> Producto:
    get_producto_ref(usuario_id, emprendimiento_id).document(producto.id_).update(asdict(producto))
    return producto

#### DELETE ENTITY BY ID
def delete_by_id(producto: Producto, usuario_id: int, emprendimiento_id: int) -> None:
    get_producto_ref(usuario_id, emprendimiento_id).document(producto.id_).delete()

#### GET PRODUCTS BY PROVEEDOR
def get_productos_by_proveedor(proveedor, usuario_id, emprendimiento_id):
    productos = get_all(usuario_id, emprendimiento_id)
    productos_proveedor = []
    for producto in productos:
        if producto.id_proveedor == proveedor.id_:
            productos_proveedor.append(producto)
    return productos_proveedor