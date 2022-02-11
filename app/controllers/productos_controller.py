from typing import List
from math import floor

from ..helpers import productos_helper
from ..database import productos_db, precios_producto_db
from ..models.models import Producto, PrecioProducto, Proveedor
from ..controllers import proveedores_controller, insumos_controller

#### CREAR
def create(producto: Producto, precio_producto: PrecioProducto, usuario_id: int, emprendimiento_id: int) -> Producto:
    ### Formatear producto
    producto_formateado = productos_helper.formatear_nombre(producto)
    ### Validar si producto con mismo nombre ya existe
    producto_encontrado = productos_db.get_by_name(producto_formateado, usuario_id, emprendimiento_id)
    productos_helper.validate_exists(producto_encontrado)
    ### Crear producto y precio producto
    producto = productos_db.create(producto, usuario_id, emprendimiento_id)
    precio_producto = precios_producto_db.create(precio_producto, usuario_id, emprendimiento_id, producto.id_)
    return producto

#### EDITAR
def edit(producto: Producto, precio_producto: PrecioProducto, usuario_id: int, emprendimiento_id: int) -> Producto:
    if precio_producto is not None:
        ultimo_precio = get_last_precio(producto, usuario_id, emprendimiento_id)
        if ultimo_precio != precio_producto:
            precios_producto_db.create(precio_producto, usuario_id, emprendimiento_id, producto.id_)
    return productos_db.update_by_id(producto, usuario_id, emprendimiento_id)

#### DELETE
def delete(producto: Producto, usuario_id: int, emprendimiento_id: int) -> None:
    precios_producto_db.delete_all(usuario_id, emprendimiento_id, producto.id_)
    productos_db.delete_by_id(producto, usuario_id, emprendimiento_id)
    return None

#### GET ALL
def get_all(usuario_id: int, emprendimiento_id: int) -> List[Producto]:
    productos = productos_db.get_all(usuario_id, emprendimiento_id)
    productos_helper.validate_empty_list(productos)
    return productos

#### GET BY ID
def get_by_id(producto_: Producto, usuario_id: int, emprendimiento_id: int) -> Producto:
    producto = productos_db.get_by_id(producto_, usuario_id, emprendimiento_id)
    return producto

#### GET LAST PRICE
def get_last_precio(producto: Producto, usuario_id: int, emprendimiento_id: int):
    precios = precios_producto_db.get_all(usuario_id, emprendimiento_id, producto.id_)
    ultimo_precio = precios[-1]
    return ultimo_precio

#### GET PRODUCTOS PROVEEDOR
def get_productos_proveedor(proveedor, usuario_id, emprendimiento_id):
    products = productos_db.get_productos_by_proveedor(proveedor, usuario_id, emprendimiento_id)
    return products

### GET PROVEEDOR NAME
def get_proveedor_name(producto: Producto, usuario_id: int, emprendimiento_id: int):
    proveedor = Proveedor(id_=producto.id_proveedor)
    proveedor_encontrado = proveedores_controller.get_by_id(proveedor, usuario_id, emprendimiento_id)
    return proveedor_encontrado


#### CALCULATE STOCK
def calculate_stock(producto: Producto, usuario_id: int, emprendimiento_id: int):

    insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
    
    productos_que_rinde = []
    for linea_insumo in producto.lineas_insumo:
        if linea_insumo != {}:
            for insumo in insumos:
                if linea_insumo['id_insumo'] == insumo.id_:
                    # Productos que rinde: stock actual del insumo sobre la cantidad necesaria
                    stock_actual_en_medida = int(insumo.stock_actual) * int(insumo.medida_presentacion)
                    productos_que_rinde.append(stock_actual_en_medida / linea_insumo['cantidad'])
    
    ### Stock actual = mínimo de los productos que rinde
    producto.stock_actual = floor(int(min(productos_que_rinde)))

    return producto

def calculate_costo(producto: Producto, usuario_id: int, emprendimiento_id: int):
    
    insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
    
    costo = 0
    for linea_insumo in producto.lineas_insumo:
        for insumo in insumos:
            if linea_insumo['id_insumo'] == insumo.id_:
                # Costo: suma de precios de insumos por la proporción de la medida del insumo según su cantidad utilizada
                costo += float(insumo.costo) * linea_insumo['cantidad'] / int(insumo.medida_presentacion)
    
    producto.costo = round(costo, 2)

    return producto