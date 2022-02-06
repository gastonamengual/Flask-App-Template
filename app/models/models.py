from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass(unsafe_hash=True)
class DBEntity():
    id_: str = None

@dataclass(unsafe_hash=True)
class Usuario(DBEntity):
    nombre: str = None
    email: str = None
    password: str = None

@dataclass(unsafe_hash=True)
class Emprendimiento(DBEntity):
    nombre: str = None
    margen_ganancia: float = None

@dataclass(unsafe_hash=True)
class Articulo(DBEntity):
    nombre: str = None
    id_proveedor: str = None
    costo: float = None
    stock_actual: int = None
    stock_minimo: int = None

@dataclass(unsafe_hash=True)
class Insumo(Articulo):
    stock_actual_en_medida: float = None
    unidad: float = None
    presentacion: str = None
    medida_presentacion: float = None

@dataclass(unsafe_hash=True)
class LineaInsumo():
    id_insumo: str = None
    cantidad: float = None

@dataclass(unsafe_hash=True)
class Producto(Articulo):
    lineas_insumo: List[LineaInsumo] = None

@dataclass(unsafe_hash=True)
class PrecioProducto():
    fecha: date = None
    precio: float = None

@dataclass(unsafe_hash=True)
class Proveedor(DBEntity):
    nombre: str = None
    telefono: str = None

@dataclass(unsafe_hash=True)
class LineaPedido():
    cantidad: int = None
    id_articulo: str = None

@dataclass(unsafe_hash=True)
class Pedido(DBEntity):
    fecha_confeccion: date = None
    fecha_recepcion: date = None
    id_proveedor: str = None
    estado: str = None
    lineas_pedido: List[LineaPedido] = None

@dataclass(unsafe_hash=True)
class Cliente(DBEntity):
    dni: str = None
    nombre: str = None
    telefono: str = None

@dataclass(unsafe_hash=True)
class LineaVenta():
    cantidad: int = None
    id_producto: str = None

@dataclass(unsafe_hash=True)
class Venta(DBEntity):
    fecha: date = None
    total: float = None
    dni_cliente: str = None
    lineas_venta: List[LineaVenta] = None

@dataclass(unsafe_hash=True)
class CostoPago():
    fecha: date = None
    importe: float = None
    
@dataclass(unsafe_hash=True)
class Costo(DBEntity):
    nombre: str = None
    frecuencia_pago: int = None
    pagos: List[CostoPago] = None
