from math import floor, ceil

from .models import *
from ..database import usuarios_db, emprendimiento_db, productos_db, insumos_db, proveedores_db, clientes_db, precios_producto_db, ventas_db, pedidos_db, costos_db

def create_test_database():

    users = usuarios_db.get_all()

    if users == []:

        ### Usuario
        usuario = Usuario(nombre='Gastón', 
                            email='ga@mail.com',
                            password='asd')
        usuario = usuarios_db.create(usuario)

        usuario_id = usuario.id_

        ### Emprendimiento
        emprendimiento = Emprendimiento(nombre='Oh Honey Nails', margen_ganancia=1.5)
        emprendimiento = emprendimiento_db.create(emprendimiento, usuario_id)

        emprendimiento_id = emprendimiento.id_

        ### Insumos
        insumo0 = Insumo(nombre='Monómero Cherimoya', id_proveedor="1", costo=1100, stock_actual=1, stock_actual_en_medida=1*100, stock_minimo=2, unidad='mililitro', presentacion="Botella", medida_presentacion=100)
        insumo1 = Insumo(nombre='Esmalte semipermanente Cherimoya', id_proveedor="1", costo=550, stock_actual=40, stock_actual_en_medida=40*15, stock_minimo=10, unidad='mililitro', presentacion="Frasco", medida_presentacion=15)
        insumo2 = Insumo(nombre='Base correctiva Cherimoya', id_proveedor="0", costo=650, stock_actual=2, stock_actual_en_medida=2*15, stock_minimo=2, unidad='mililitro', presentacion="Frasco", medida_presentacion=15)
        insumo3 = Insumo(nombre='Alcohol', id_proveedor="2", costo=100, stock_actual=1, stock_actual_en_medida=1*500, stock_minimo=2, unidad='mililitro', presentacion="Botella", medida_presentacion=500)
        insumo4 = Insumo(nombre='Algodón', id_proveedor="2", costo=80, stock_actual=1, stock_actual_en_medida=1*140, stock_minimo=1, unidad='gramos', presentacion='Paquete', medida_presentacion=140)
        insumo5 = Insumo(nombre='Infinite Shine', id_proveedor="0", costo=900, stock_actual=10, stock_actual_en_medida=10*15, stock_minimo=10, unidad='mililitro', presentacion='Frasco', medida_presentacion=15)
        insumo6 = Insumo(nombre='Guantes', id_proveedor="0", costo=2000, stock_actual=1, stock_actual_en_medida=1*50, stock_minimo=1, unidad='par', presentacion='Caja', medida_presentacion=50)
        insumo7 = Insumo(nombre='Removedor', id_proveedor="2", costo=870, stock_actual=1, stock_actual_en_medida=1*500, stock_minimo=2, unidad='mililitro', presentacion='Botella', medida_presentacion=500)
        insumo8 = Insumo(nombre='Acrílico clear Mia Secret', id_proveedor="0", costo=4290, stock_actual=1, stock_actual_en_medida=1*118, stock_minimo=1, unidad='gramos', presentacion='Frasco', medida_presentacion=118)
        insumo9 = Insumo(nombre='Deco', id_proveedor="1", costo=350, stock_actual=5, stock_actual_en_medida=5*10, stock_minimo=10, unidad='gramos', presentacion='Frasco', medida_presentacion=10)

        insumos = [insumo0, insumo1, insumo2, insumo3, insumo4, insumo5, insumo6, insumo7, insumo8, insumo9]
        for insumo in insumos:
            insumos_db.create(insumo, usuario_id, emprendimiento_id)

        ### Productos
        # 10
        producto10 = Producto(nombre="Esmaltado semipermanente Chanel",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="1", cantidad=0.5), 
                                        LineaInsumo(id_insumo="3", cantidad=5), 
                                        LineaInsumo(id_insumo="6", cantidad=1), 
                                        LineaInsumo(id_insumo="9", cantidad=2)])
        precio_producto100 = PrecioProducto(fecha='2021-11-09', precio=650)
        precio_producto101 = PrecioProducto(fecha='2022-01-09', precio=700)

        # 11
        producto11 = Producto(nombre="Esmaltado semipermanente Tiffany",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="1", cantidad=0.5),
                                        LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="6", cantidad=1),
                                        LineaInsumo(id_insumo="9", cantidad=5)])
        precio_producto110 = PrecioProducto(fecha='2021-11-09', precio=750)
        precio_producto111 = PrecioProducto(fecha='2022-01-09', precio=800)
        
        # 12
        producto12 = Producto(nombre="Uñas esculpidas en acrílico",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="0", cantidad=10), 
                                        LineaInsumo(id_insumo="1", cantidad=0.5), 
                                        LineaInsumo(id_insumo="6", cantidad=1), 
                                        LineaInsumo(id_insumo="8", cantidad=10),
                                        LineaInsumo(id_insumo="9", cantidad=2)])
        precio_producto120 = PrecioProducto(fecha='2021-11-09', precio=750)
        precio_producto121 = PrecioProducto(fecha='2022-01-09', precio=800)
        
        # 13
        producto13 = Producto(nombre="Belleza de pies con esmaltado",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="5", cantidad=4), 
                                        LineaInsumo(id_insumo="6", cantidad=1)])
        precio_producto130 = PrecioProducto(fecha='2021-11-09', precio=550)
        precio_producto131 = PrecioProducto(fecha='2022-01-09', precio=600)
        
        # 14
        producto14 = Producto(nombre="Infinite shine",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="5", cantidad=4), 
                                        LineaInsumo(id_insumo="6", cantidad=1)])
        precio_producto140 = PrecioProducto(fecha='2021-11-09', precio=600)
        precio_producto141 = PrecioProducto(fecha='2022-01-09', precio=650)
        
        # 15
        producto15 = Producto(nombre="Remoción",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="4", cantidad=5),
                                        LineaInsumo(id_insumo="7", cantidad=10)])
        precio_producto150 = PrecioProducto(fecha='2021-11-09', precio=350)
        precio_producto151 = PrecioProducto(fecha='2022-01-09', precio=400)
        
        # 16
        producto16 = Producto(nombre="Capping con semi Chanel",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="1", cantidad=0.5),
                                        LineaInsumo(id_insumo="2", cantidad=0.5)])
        precio_producto160 = PrecioProducto(fecha='2021-11-09', precio=650)
        precio_producto161 = PrecioProducto(fecha='2022-01-09', precio=730)
        
        productos = [producto10, producto11, producto12, producto13, producto14, producto15, producto16]
        precios_producto = [[precio_producto100, precio_producto101], 
                            [precio_producto110, precio_producto111], 
                            [precio_producto120, precio_producto121],
                            [precio_producto130, precio_producto131], 
                            [precio_producto140, precio_producto141], 
                            [precio_producto150, precio_producto151], 
                            [precio_producto160, precio_producto161]]

        for producto in productos:
            productos_que_rinde = []
            costo = 0
            for linea_insumo in producto.lineas_insumo:
                insumo_ = Insumo(id_=linea_insumo.id_insumo)
                insumo = insumos_db.get_by_id(insumo_, usuario_id, emprendimiento_id)
                
                stock_actual_en_medida = int(insumo.stock_actual) * int(insumo.medida_presentacion)
                productos_que_rinde.append(stock_actual_en_medida / linea_insumo.cantidad)
                costo += float(insumo.costo) * linea_insumo.cantidad / int(insumo.medida_presentacion)

            producto.stock_actual = floor(int(min(productos_que_rinde)))
            producto.costo = ceil(costo)

        for producto, precios in zip(productos, precios_producto):
            producto = productos_db.create(producto, usuario_id, emprendimiento_id)
            for precio in precios:
                precios_producto_db.create(precio, usuario_id, emprendimiento_id, producto.id_)

        ### Proveedores
        proveedor0 = Proveedor(nombre="E&M")
        proveedor1 = Proveedor(nombre="Lan Lan")
        proveedor2 = Proveedor(nombre="Bloom")
        proveedor3 = Proveedor(nombre="NailsByLu")
        proveedor4 = Proveedor(nombre="EgoNails")
        proveedor5 = Proveedor(nombre="Manima SRL")
        proveedor6 = Proveedor(nombre="Semia Insumos")
        proveedor7 = Proveedor(nombre="DeUñas Tienda")

        proveedores = [proveedor0, proveedor1, proveedor2, proveedor3, proveedor4, proveedor5, proveedor6, proveedor7]
        
        for proveedor in proveedores:
            proveedores_db.create(proveedor, usuario_id, emprendimiento_id)

        ### Clientes
        clientes = [Cliente(dni="30442203", nombre='Agostina'),
                    Cliente(dni="22778223", nombre='Agustina'),
                    Cliente(dni="42621496", nombre='Angie'),
                    Cliente(dni="41624516", nombre='Brenda'),
                    Cliente(dni="30271815", nombre='Camila'),
                    Cliente(dni="35138846", nombre='Candela F'),
                    Cliente(dni="30439345", nombre='Candela T'),
                    Cliente(dni="38372625", nombre='Carolina'),
                    Cliente(dni="32219767", nombre='Catalina'),
                    Cliente(dni="41758888", nombre='Celeste'),
                    Cliente(dni="25921968", nombre='Clara'),
                    Cliente(dni="33519135", nombre='Claudia'),
                    Cliente(dni="21395149", nombre='Cristian'),
                    Cliente(dni="35274198", nombre='Daiana'),
                    Cliente(dni="24323076", nombre='Debora'),
                    Cliente(dni="25863042", nombre='Eliana'),
                    Cliente(dni="29873092", nombre='Elisa'),
                    Cliente(dni="39872027", nombre='Fabiola'),
                    Cliente(dni="40917395", nombre='Florencia'),
                    Cliente(dni="30987292", nombre='Felicitas'),
                    Cliente(dni="41011409", nombre='Graciela'),
                    Cliente(dni="28308716", nombre='Isabella'),
                    Cliente(dni="37293092", nombre='Jesica'),
                    Cliente(dni="37155787", nombre='Karen'),
                    Cliente(dni="38720982", nombre='Leonila'),
                    Cliente(dni="39013475", nombre='Laura Callejas'),
                    Cliente(dni="24585866", nombre='Laura Consiglio'),
                    Cliente(dni="38495049", nombre='Magalí'),
                    Cliente(dni="37826585", nombre='Malena'),
                    Cliente(dni="35652898", nombre='Manuela'),
                    Cliente(dni="42416251", nombre='Micaela'),
                    Cliente(dni="22990677", nombre='Milagros'),
                    Cliente(dni="26044688", nombre='Nahir'),
                    Cliente(dni="25047621", nombre='Natalia F'),
                    Cliente(dni="37027641", nombre='Natalia'),
                    Cliente(dni="28386573", nombre='Olivia'),
                    Cliente(dni="37264093", nombre='Pamela'),
                    Cliente(dni="41582166", nombre='Paula'),
                    Cliente(dni="25006107", nombre='Rocio'),
                    Cliente(dni="37527495", nombre='Rocío'),
                    Cliente(dni="26141764", nombre='Silvina'),
                    Cliente(dni="30099748", nombre='Solana'),
                    Cliente(dni="22298393", nombre='Valentina'),
                    Cliente(dni="32248327", nombre='Vanessa'),
                    Cliente(dni="34909827", nombre='Yamila'),]

        for cliente in clientes:
            clientes_db.create(cliente, usuario_id, emprendimiento_id)

        ### Ventas
        ventas = [Venta(fecha='2021-10-01', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-01', total=1400, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=2, id_producto='10')]),
                  Venta(fecha='2021-10-01', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-04', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-04', total=1460, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=2, id_producto='16')]),
                  Venta(fecha='2021-10-05', total=700, dni_cliente="25921968", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-06', total=700, dni_cliente="41011409", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-06', total=650, dni_cliente="22778223", lineas_venta=[LineaVenta(cantidad=1, id_producto='14')]),
                  Venta(fecha='2021-10-07', total=730, dni_cliente="40917395", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-08', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-08', total=800, dni_cliente="30099748", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-11', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-11', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-12', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-12', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-13', total=700, dni_cliente="41758888", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-13', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-13', total=800, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-14', total=700, dni_cliente="35274198", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-15', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-15', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-15', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-18', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-18', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-19', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-19', total=730, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-19', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-20', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-20', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-21', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-21', total=700, dni_cliente="37293092", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-21', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-22', total=1400, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-22', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-22', total=850, dni_cliente="32219767", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-25', total=730, dni_cliente="25863042", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-10-25', total=800, dni_cliente="22298393", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-25', total=700, dni_cliente="26141764", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-26', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-27', total=1230, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-10-27', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-28', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-10-28', total=850, dni_cliente="25006107", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-10-29', total=600, dni_cliente="37264093", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),

                  Venta(fecha='2021-11-01', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-01', total=700, dni_cliente="41758888", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-01', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-02', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-02', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-02', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-02', total=1460, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=2, id_producto='16')]),
                  Venta(fecha='2021-11-03', total=700, dni_cliente="25921968", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-03', total=1400, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=2, id_producto='10')]),
                  Venta(fecha='2021-11-03', total=700, dni_cliente="35274198", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-03', total=700, dni_cliente="41011409", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-04', total=650, dni_cliente="22778223", lineas_venta=[LineaVenta(cantidad=1, id_producto='14')]),
                  Venta(fecha='2021-11-04', total=730, dni_cliente="40917395", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-04', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-04', total=800, dni_cliente="30099748", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-05', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-05', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-08', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-08', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-08', total=800, dni_cliente="22298393", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-08', total=800, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-09', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-09', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-10', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-10', total=730, dni_cliente="24323076", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-11', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-11', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-11', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-11', total=850, dni_cliente="25006107", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-11', total=850, dni_cliente="32219767", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-12', total=730, dni_cliente="25863042", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-12', total=730, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-15', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-15', total=1400, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-15', total=700, dni_cliente="26141764", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-15', total=650, dni_cliente="22778223", lineas_venta=[LineaVenta(cantidad=1, id_producto='14')]),
                  Venta(fecha='2021-11-15', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-16', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-16', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-16', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-16', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-17', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-17', total=600, dni_cliente="37264093", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-11-17', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-17', total=700, dni_cliente="37027641", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-17', total=700, dni_cliente="35138846", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-18', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-18', total=1230, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-11-19', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-19', total=700, dni_cliente="37293092", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-19', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-19', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-19', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-22', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-22', total=730, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-23', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-23', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-23', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-24', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-24', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-24', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-25', total=800, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-25', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-25', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-25', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-26', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-26', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-29', total=800, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-29', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-11-29', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-29', total=850, dni_cliente="25047621", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-11-30', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-30', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-30', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-11-30', total=2860, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=2, id_producto='16'), LineaVenta(cantidad=2, id_producto='13')]),
                  Venta(fecha='2021-11-30', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  

                  Venta(fecha='2021-12-01', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-01', total=450, dni_cliente="30439345", lineas_venta=[LineaVenta(cantidad=1, id_producto='15')]),
                  Venta(fecha='2021-12-01', total=700, dni_cliente="21395149", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-01', total=600, dni_cliente="37264093", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-01', total=700, dni_cliente="35138846", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-02', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-02', total=800, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-02', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-02', total=2860, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=2, id_producto='16'), LineaVenta(cantidad=2, id_producto='13')]),
                  Venta(fecha='2021-12-02', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-02', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-03', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-03', total=800, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-03', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-06', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-06', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-06', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-07', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-07', total=700, dni_cliente="32248327", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-07', total=700, dni_cliente="38495049", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-07', total=850, dni_cliente="25047621", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-07', total=730, dni_cliente="40917395", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-07', total=1230, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-07', total=600, dni_cliente="37264093", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-08', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-08', total=700, dni_cliente="37027641", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-08', total=850, dni_cliente="30439345", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-09', total=1230, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-09', total=700, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-09', total=730, dni_cliente="25863042", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-09', total=850, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-09', total=730, dni_cliente="34909827", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-09', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-10', total=700, dni_cliente="41624516", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-10', total=730, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-10', total=850, dni_cliente="30987292", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-13', total=730, dni_cliente="38720982", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-13', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-13', total=700, dni_cliente="34909827", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-13', total=850, dni_cliente="30439345", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-13', total=850, dni_cliente="25006107", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-14', total=700, dni_cliente="39872027", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-14', total=600, dni_cliente="29873092", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-14', total=730, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-15', total=700, dni_cliente="35138846", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-15', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-15', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-15', total=700, dni_cliente="37293092", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-15', total=1230, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-16', total=850, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-16', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-16', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-16', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-16', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-16', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-16', total=700, dni_cliente="41758888", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-17', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-17', total=700, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-17', total=800, dni_cliente="30271815", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-17', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-17', total=2860, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=2, id_producto='16'), LineaVenta(cantidad=2, id_producto='13')]),
                  Venta(fecha='2021-12-17', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-17', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-20', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-20', total=800, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-20', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-20', total=730, dni_cliente="40917395", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-20', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-21', total=800, dni_cliente="30099748", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-21', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-21', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-21', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-21', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-22', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-22', total=850, dni_cliente="30439345", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-22', total=850, dni_cliente="25006107", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-22', total=730, dni_cliente="38720982", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-23', total=1230, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='16'), LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-23', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-23', total=730, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-24', total=700, dni_cliente="39872027", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-24', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-24', total=600, dni_cliente="29873092", lineas_venta=[LineaVenta(cantidad=1, id_producto='13')]),
                  Venta(fecha='2021-12-24', total=700, dni_cliente="34909827", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-24', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-24', total=850, dni_cliente="22990677", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-24', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-27', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-27', total=700, dni_cliente="37293092", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-27', total=700, dni_cliente="35138846", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-27', total=700, dni_cliente="42416251", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-27', total=800, dni_cliente="35652898", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-27', total=800, dni_cliente="28308716", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-28', total=700, dni_cliente="35274198", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-28', total=730, dni_cliente="42621496", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-28', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-28', total=700, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-28', total=700, dni_cliente="41758888", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-29', total=700, dni_cliente="37826585", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-29', total=1400, dni_cliente="33519135", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-29', total=800, dni_cliente="22298393", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-30', total=700, dni_cliente="30442203", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-30', total=730, dni_cliente="37155787", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-30', total=850, dni_cliente="32219767", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-30', total=700, dni_cliente="38495049", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-30', total=700, dni_cliente="37527495", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-30', total=730, dni_cliente="25863042", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-30', total=850, dni_cliente="38372625", lineas_venta=[LineaVenta(cantidad=1, id_producto='12')]),
                  Venta(fecha='2021-12-31', total=700, dni_cliente="32248327", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-31', total=700, dni_cliente="24585866", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-31', total=700, dni_cliente="41582166", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-31', total=700, dni_cliente="39013475", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-31', total=700, dni_cliente="37293092", lineas_venta=[LineaVenta(cantidad=1, id_producto='10')]),
                  Venta(fecha='2021-12-31', total=730, dni_cliente="28386573", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),
                  Venta(fecha='2021-12-31', total=730, dni_cliente="26044688", lineas_venta=[LineaVenta(cantidad=1, id_producto='16')]),    
        ]

        for venta in ventas:
            ventas_db.create(venta, usuario_id, emprendimiento_id)
        
        ### Pedidos
        pedidos = [
                  Pedido(fecha_confeccion='2021-10-04', fecha_recepcion='2021-10-05', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='2'), LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-10-08', fecha_recepcion='2021-10-08', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='0'), LineaPedido(cantidad=8, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-10-11', fecha_recepcion='2021-10-12', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=1, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-10-12', fecha_recepcion=None, id_proveedor='0', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='2'), LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-10-13', fecha_recepcion='2021-10-13', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='2'), LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-10-15', fecha_recepcion='2021-10-17', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='0'), LineaPedido(cantidad=8, id_articulo='1'), LineaPedido(cantidad=10, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-10-18', fecha_recepcion='2021-10-20', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-10-20', fecha_recepcion='2021-10-20', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='2'), LineaPedido(cantidad=11, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-10-21', fecha_recepcion=None, id_proveedor='1', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='0'), LineaPedido(cantidad=11, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-10-22', fecha_recepcion='2021-10-23', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='0'), LineaPedido(cantidad=11, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-10-27', fecha_recepcion='2021-10-28', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-10-29', fecha_recepcion='2021-10-31', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='2'), LineaPedido(cantidad=12, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-01', fecha_recepcion='2021-11-03', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='0'), LineaPedido(cantidad=11, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-11-03', fecha_recepcion='2021-11-03', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-11-05', fecha_recepcion='2021-11-07', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='2'), LineaPedido(cantidad=11, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-08', fecha_recepcion='2021-11-08', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=11, id_articulo='1'), LineaPedido(cantidad=11, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-11-10', fecha_recepcion='2021-11-10', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-11-11', fecha_recepcion=None, id_proveedor='0', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='2'), LineaPedido(cantidad=12, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-12', fecha_recepcion='2021-11-14', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='2'), LineaPedido(cantidad=12, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-15', fecha_recepcion='2021-11-17', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='0'), LineaPedido(cantidad=9, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-11-17', fecha_recepcion='2021-11-19', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-11-19', fecha_recepcion='2021-11-19', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='2'), LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-22', fecha_recepcion='2021-11-24', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='0'), LineaPedido(cantidad=9, id_articulo='1'), LineaPedido(cantidad=10, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-11-24', fecha_recepcion='2021-11-26', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-11-26', fecha_recepcion='2021-11-27', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='2'), LineaPedido(cantidad=10, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-11-27', fecha_recepcion=None, id_proveedor='1', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='0'), LineaPedido(cantidad=9, id_articulo='1'), LineaPedido(cantidad=10, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-11-29', fecha_recepcion='2021-11-30', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='0'), LineaPedido(cantidad=9, id_articulo='1'), LineaPedido(cantidad=10, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-12-01', fecha_recepcion='2021-12-02', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-03', fecha_recepcion='2021-12-04', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='2'), LineaPedido(cantidad=10, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-12-06', fecha_recepcion='2021-12-06', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='0'), LineaPedido(cantidad=10, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-12-08', fecha_recepcion='2021-12-09', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=1, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-10', fecha_recepcion='2021-12-11', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-12-13', fecha_recepcion='2021-12-13', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='0'), LineaPedido(cantidad=11, id_articulo='1'), LineaPedido(cantidad=9, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-12-13', fecha_recepcion=None, id_proveedor='2', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-15', fecha_recepcion='2021-12-17', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='3'), LineaPedido(cantidad=1, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-17', fecha_recepcion='2021-12-17', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='2'), LineaPedido(cantidad=10, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6'), LineaPedido(cantidad=2, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-12-20', fecha_recepcion='2021-12-20', id_proveedor='1', estado='recibido', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='0'), LineaPedido(cantidad=9, id_articulo='1'), LineaPedido(cantidad=10, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-12-22', fecha_recepcion='2021-12-24', id_proveedor='2', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=3, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-24', fecha_recepcion='2021-12-26', id_proveedor='0', estado='recibido', lineas_pedido=[LineaPedido(cantidad=1, id_articulo='2'), LineaPedido(cantidad=9, id_articulo='5'), LineaPedido(cantidad=1, id_articulo='6'), LineaPedido(cantidad=1, id_articulo='8')]),
                  Pedido(fecha_confeccion='2021-12-27', fecha_recepcion=None, id_proveedor='1', estado='pendiente', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='0'), LineaPedido(cantidad=12, id_articulo='1'), LineaPedido(cantidad=12, id_articulo='9')]),
                  Pedido(fecha_confeccion='2021-12-18', fecha_recepcion=None, id_proveedor='2', estado='cancelado', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=2, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-29', fecha_recepcion=None, id_proveedor='2', estado='pendiente', lineas_pedido=[LineaPedido(cantidad=2, id_articulo='3'), LineaPedido(cantidad=2, id_articulo='4'), LineaPedido(cantidad=2, id_articulo='7')]),
                  Pedido(fecha_confeccion='2021-12-31', fecha_recepcion=None, id_proveedor='0', estado='pendiente', lineas_pedido=[LineaPedido(cantidad=3, id_articulo='2'), LineaPedido(cantidad=12, id_articulo='5'), LineaPedido(cantidad=2, id_articulo='6')]),    
        ]

        for pedido in pedidos:
            pedidos_db.create(pedido, usuario_id, emprendimiento_id)

        ### Costos
        costos = [Costo(nombre='EPE', frecuencia_pago=2, pagos=[CostoPago(fecha='2021-10-03', importe=2000), CostoPago(fecha='2021-12-05', importe=2400)]),
                  Costo(nombre='Internet Fibertel', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-4', importe=1072), CostoPago(fecha='2021-11-4', importe=1235), CostoPago(fecha='2021-12-5', importe=1363)]),
                  Costo(nombre='Monitoreo SurGuard', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-4', importe=1056), CostoPago(fecha='2021-11-6', importe=1182), CostoPago(fecha='2021-12-6', importe=1288)]),
                  Costo(nombre='Agua', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-2', importe=1040), CostoPago(fecha='2021-11-8', importe=1156), CostoPago(fecha='2021-12-8', importe=1388)]),
                  Costo(nombre='Gas', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-5', importe=189), CostoPago(fecha='2021-11-3', importe=224), CostoPago(fecha='2021-12-5', importe=277)]),
                  Costo(nombre='Monotributo', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-7', importe=1689), CostoPago(fecha='2021-11-5', importe=1809), CostoPago(fecha='2021-12-5', importe=1813)]),
                  Costo(nombre='Impuestos', frecuencia_pago=1, pagos=[CostoPago(fecha='2021-10-4', importe=1208), CostoPago(fecha='2021-11-2', importe=1212), CostoPago(fecha='2021-12-', importe=1259)]),
        ]

        for costo in costos:
            costos_db.create(costo, usuario_id, emprendimiento_id)