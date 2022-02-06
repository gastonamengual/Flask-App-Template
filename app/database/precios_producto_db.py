from dataclasses import asdict
from typing import List, Optional

from ..models.models import PrecioProducto, Producto
from .base_db import db

def get_precios_ref(usuario_id, emprendimiento_id, producto_id):
    return db.collection(u"Usuarios").document(usuario_id) \
           .collection(u"Emprendimientos").document(emprendimiento_id) \
           .collection(u"Productos").document(producto_id) \
           .collection(u'Precios')

#### CREATE
def create(precio_producto: PrecioProducto, usuario_id: int, emprendimiento_id: int, producto_id: int) -> PrecioProducto:
    precio_producto = get_precios_ref(usuario_id, emprendimiento_id, producto_id).document(precio_producto.fecha).set(asdict(precio_producto))
    return precio_producto


#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int, producto_id: int) -> List[Producto]:

    docs = get_precios_ref(usuario_id, emprendimiento_id, producto_id).get()
    if docs == []:
        return []
    
    results = []
    for doc in docs:
        results.append(PrecioProducto(**doc.to_dict()))
    
    return results

#### DELETE ALL
def delete_all(usuario_id: int, emprendimiento_id: int, producto_id: int):
    docs = get_precios_ref(usuario_id, emprendimiento_id, producto_id).stream()
    for doc in docs:
        doc.reference.delete()