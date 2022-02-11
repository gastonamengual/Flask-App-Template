from math import floor

from .models import *
from ..database import usuarios_db, emprendimiento_db, productos_db, insumos_db, proveedores_db, clientes_db, precios_producto_db, ventas_db, pedidos_db, costos_db

def create_test_database():

    users = usuarios_db.get_all()

    if users == []:

        ### Usuario
        usuario = Usuario(nombre='Gastón', 
                            email='gastonamengual@icloud.com',
                            password='asd')
        usuario = usuarios_db.create(usuario)

        usuario_id = usuario.id_

        ### Emprendimiento
        emprendimiento = Emprendimiento(nombre='Oh Honey Nails', margen_ganancia=1.5)
        emprendimiento = emprendimiento_db.create(emprendimiento, usuario_id)

        emprendimiento_id = emprendimiento.id_

        ### Insumos
        insumo0 = Insumo(nombre='Monómero Cherimoya', id_proveedor="1", costo=1100.23, stock_actual=1, stock_actual_en_medida=1*100, stock_minimo=2, unidad='mililitro', presentacion="Botella", medida_presentacion=100)
        insumo1 = Insumo(nombre='Esmalte semipermanente Cherimoya', id_proveedor="1", costo=550.45, stock_actual=40, stock_actual_en_medida=40*15, stock_minimo=10, unidad='mililitro', presentacion="Frasco", medida_presentacion=15)
        insumo2 = Insumo(nombre='Base correctiva Cherimoya', id_proveedor="0", costo=650.34, stock_actual=2, stock_actual_en_medida=2*15, stock_minimo=2, unidad='mililitro', presentacion="Frasco", medida_presentacion=15)
        insumo3 = Insumo(nombre='Alcohol', id_proveedor="2", costo=100.56, stock_actual=1, stock_actual_en_medida=1*500, stock_minimo=2, unidad='mililitro', presentacion="Botella", medida_presentacion=500)
        insumo4 = Insumo(nombre='Algodón', id_proveedor="2", costo=80.02, stock_actual=1, stock_actual_en_medida=1*140, stock_minimo=1, unidad='gramos', presentacion='Paquete', medida_presentacion=140)
        insumo5 = Insumo(nombre='Infinite Shine', id_proveedor="0", costo=900.24, stock_actual=10, stock_actual_en_medida=10*15, stock_minimo=10, unidad='mililitro', presentacion='Frasco', medida_presentacion=15)
        insumo6 = Insumo(nombre='Guantes', id_proveedor="0", costo=2000.25, stock_actual=1, stock_actual_en_medida=1*50, stock_minimo=1, unidad='par', presentacion='Caja', medida_presentacion=50)
        insumo7 = Insumo(nombre='Removedor', id_proveedor="2", costo=870.94, stock_actual=1, stock_actual_en_medida=1*500, stock_minimo=2, unidad='mililitro', presentacion='Botella', medida_presentacion=500)
        insumo8 = Insumo(nombre='Acrílico clear Mia Secret', id_proveedor="0", costo=4290.23, stock_actual=1, stock_actual_en_medida=1*118, stock_minimo=1, unidad='gramos', presentacion='Frasco', medida_presentacion=118)
        insumo9 = Insumo(nombre='Deco', id_proveedor="1", costo=350.43, stock_actual=5, stock_actual_en_medida=5*10, stock_minimo=10, unidad='gramos', presentacion='Frasco', medida_presentacion=10)

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
        precio_producto100 = PrecioProducto(fecha='2021-11-09', precio=650.23)
        precio_producto101 = PrecioProducto(fecha='2022-01-09', precio=700.34)

        # 11
        producto11 = Producto(nombre="Esmaltado semipermanente Tiffany",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="1", cantidad=0.5),
                                        LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="6", cantidad=1),
                                        LineaInsumo(id_insumo="9", cantidad=5)])
        precio_producto110 = PrecioProducto(fecha='2021-11-09', precio=750.65)
        precio_producto111 = PrecioProducto(fecha='2022-01-09', precio=800.26)
        
        # 12
        producto12 = Producto(nombre="Uñas esculpidas en acrílico",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="0", cantidad=10), 
                                        LineaInsumo(id_insumo="1", cantidad=0.5), 
                                        LineaInsumo(id_insumo="6", cantidad=1), 
                                        LineaInsumo(id_insumo="8", cantidad=10),
                                        LineaInsumo(id_insumo="9", cantidad=2)])
        precio_producto120 = PrecioProducto(fecha='2021-11-09', precio=750.92)
        precio_producto121 = PrecioProducto(fecha='2022-01-09', precio=800.83)
        
        # 13
        producto13 = Producto(nombre="Belleza de pies con esmaltado",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="5", cantidad=4), 
                                        LineaInsumo(id_insumo="6", cantidad=1)])
        precio_producto130 = PrecioProducto(fecha='2021-11-09', precio=550.28)
        precio_producto131 = PrecioProducto(fecha='2022-01-09', precio=600.93)
        
        # 14
        producto14 = Producto(nombre="Infinite shine",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="3", cantidad=5),
                                        LineaInsumo(id_insumo="5", cantidad=4), 
                                        LineaInsumo(id_insumo="6", cantidad=1)])
        precio_producto140 = PrecioProducto(fecha='2021-11-09', precio=600.23)
        precio_producto141 = PrecioProducto(fecha='2022-01-09', precio=650.92)
        
        # 15
        producto15 = Producto(nombre="Remoción",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="4", cantidad=5),
                                        LineaInsumo(id_insumo="7", cantidad=10)])
        precio_producto150 = PrecioProducto(fecha='2021-11-09', precio=350.02)
        precio_producto151 = PrecioProducto(fecha='2022-01-09', precio=400.25)
        
        # 16
        producto16 = Producto(nombre="Capping con semi Chanel",
                            stock_minimo = 10,
                            lineas_insumo=[LineaInsumo(id_insumo="1", cantidad=0.5),
                                        LineaInsumo(id_insumo="2", cantidad=0.5)])
        precio_producto160 = PrecioProducto(fecha='2021-11-09', precio=650.23)
        precio_producto161 = PrecioProducto(fecha='2022-01-09', precio=730.54)
        
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
            producto.costo = round(costo, 2)

        for producto, precios in zip(productos, precios_producto):
            producto = productos_db.create(producto, usuario_id, emprendimiento_id)
            for precio in precios:
                precios_producto_db.create(precio, usuario_id, emprendimiento_id, producto.id_)

        ### Proveedores
        proveedor0 = Proveedor(nombre="E&M", telefono="3414277845")
        proveedor1 = Proveedor(nombre="Lan Lan", telefono="3413586904")
        proveedor2 = Proveedor(nombre="Bloom", telefono="3415222023")
        proveedor3 = Proveedor(nombre="NailsByLu", telefono="3414590549")
        proveedor4 = Proveedor(nombre="EgoNails", telefono="3416326994")
        proveedor5 = Proveedor(nombre="Manima SRL", telefono="3415355901")
        proveedor6 = Proveedor(nombre="Semia Insumos", telefono="3414451211")
        proveedor7 = Proveedor(nombre="DeUñas Tienda", telefono="3414918455")

        proveedores = [proveedor0, proveedor1, proveedor2, proveedor3, proveedor4, proveedor5, proveedor6, proveedor7]
        
        for proveedor in proveedores:
            proveedores_db.create(proveedor, usuario_id, emprendimiento_id)

        ### Clientes
        clientes = [Cliente(dni="30442203", nombre='Agostina', telefono="3416786012"),
                    Cliente(dni="22778223", nombre='Agustina', telefono="3415940017"),
                    Cliente(dni="42621496", nombre='Angie', telefono="3414977604"),
                    Cliente(dni="41624516", nombre='Brenda', telefono="3416916709"),
                    Cliente(dni="30271815", nombre='Camila', telefono="3413196006"),
                    Cliente(dni="35138846", nombre='Candela F', telefono="3414585789"),
                    Cliente(dni="30439345", nombre='Candela T', telefono="3413752447"),
                    Cliente(dni="38372625", nombre='Carolina', telefono="3414470363"),
                    Cliente(dni="32219767", nombre='Catalina', telefono="3416962727"),
                    Cliente(dni="41758888", nombre='Celeste', telefono="3414277845"),
                    Cliente(dni="25921968", nombre='Clara', telefono="3413586904"),
                    Cliente(dni="33519135", nombre='Claudia', telefono="3415222023"),
                    Cliente(dni="21395149", nombre='Cristian', telefono="3414590549"),
                    Cliente(dni="35274198", nombre='Daiana', telefono="3416326994"),
                    Cliente(dni="24323076", nombre='Debora', telefono="3415355901"),
                    Cliente(dni="25863042", nombre='Eliana', telefono="3414451211"),
                    Cliente(dni="29873092", nombre='Elisa', telefono="3414918455"),
                    Cliente(dni="39872027", nombre='Fabiola', telefono="3414301636"),
                    Cliente(dni="40917395", nombre='Florencia', telefono="3414418944"),
                    Cliente(dni="30987292", nombre='Felicitas', telefono="3413860853"),
                    Cliente(dni="41011409", nombre='Graciela', telefono="3415813503"),
                    Cliente(dni="28308716", nombre='Isabella', telefono="3414722099"),
                    Cliente(dni="37293092", nombre='Jesica', telefono="3413064700"),
                    Cliente(dni="37155787", nombre='Karen', telefono="3415409309"),
                    Cliente(dni="38720982", nombre='Leonila', telefono="3413212614"),
                    Cliente(dni="39013475", nombre='Laura Callejas', telefono="3416874495"),
                    Cliente(dni="24585866", nombre='Laura Consiglio', telefono="3413338718"),
                    Cliente(dni="38495049", nombre='Magalí', telefono="3413803768"),
                    Cliente(dni="37826585", nombre='Malena', telefono="3413929891"),
                    Cliente(dni="35652898", nombre='Manuela', telefono="3414946162"),
                    Cliente(dni="42416251", nombre='Micaela', telefono="3415909096"),
                    Cliente(dni="22990677", nombre='Milagros', telefono="3415792629"),
                    Cliente(dni="26044688", nombre='Nahir', telefono="3416409576"),
                    Cliente(dni="25047621", nombre='Natalia F', telefono="3414724930"),
                    Cliente(dni="37027641", nombre='Natalia', telefono="3415574026"),
                    Cliente(dni="28386573", nombre='Olivia', telefono="3415367389"),
                    Cliente(dni="37264093", nombre='Pamela', telefono="3413961108"),
                    Cliente(dni="41582166", nombre='Paula', telefono="3415751130"),
                    Cliente(dni="25006107", nombre='Rocio', telefono="3416453330"),
                    Cliente(dni="37527495", nombre='Rocío', telefono="3413583757"),
                    Cliente(dni="26141764", nombre='Silvina', telefono="3416309018"),
                    Cliente(dni="30099748", nombre='Solana', telefono="3413171618"),
                    Cliente(dni="22298393", nombre='Valentina', telefono="3413101095"),
                    Cliente(dni="32248327", nombre='Vanessa', telefono="3414546929"),
                    Cliente(dni="34909827", nombre='Yamila', telefono="3415723582"),]

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