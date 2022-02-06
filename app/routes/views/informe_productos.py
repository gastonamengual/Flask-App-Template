from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...controllers import ventas_controller, productos_controller, emprendimientos_controller, pedidos_controller
from ...models.models import Emprendimiento, Producto

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns

informe_productos_scope = Blueprint('informe_productos', __name__, url_prefix='/informe_productos')
@informe_productos_scope.post("/informe_productos_dispatcher")
def informe_productos_dispatcher():
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    data = request.form
    fecha_inicio = pd.to_datetime(data['fecha_inicio'])
    fecha_fin = pd.to_datetime(data['fecha_fin'])
    
    producto_id = request.form.get('producto_id')
    producto_ = Producto(id_=producto_id)
    producto_ingresado = productos_controller.get_by_id(producto_, usuario_id, emprendimiento_id)
    
    if request.form['action'] == 'global':
        return informe_global(usuario_id, emprendimiento, fecha_inicio, fecha_fin)
    elif request.form['action'] == 'producto_ingresado':
        if producto_id is not None:
            return informe_producto_ingresado(usuario_id, emprendimiento, fecha_inicio, fecha_fin, producto_ingresado)
        else:
            flash('Debe seleccionar un producto')
            return redirect(url_for('views.informes_views.informes'))

################################################

def plot_top_total(df):
    
    plt.figure(figsize=(16, 3))
    sns.barplot(x=df['total'], y=df['nombre'])
    plt.ylabel('')
    plt.xlabel('Monto total')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/productos_ranking_ganancia.png', bbox_inches='tight')

    #########

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.2f}%".format(pct, absolute)

    plt.figure(figsize=(8, 8))
    wedges, _, autotexts = plt.pie(df['porcentaje'], textprops=dict(color="w"), autopct=lambda pct: func(pct, df['porcentaje']), normalize=True)
    plt.legend(wedges, df['nombre'], loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=14, weight="bold")
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/productos_ranking_pie.png', bbox_inches='tight')

def plot_top_ventas(df):
    plt.figure(figsize=(16, 3))
    sns.barplot(x=df['ventas'], y=df['nombre'])
    plt.ylabel('')
    plt.xlabel('Cantidad de ventas')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/productos_ranking_cantidad.png', bbox_inches='tight')

################################################

def informe_global(usuario_id, emprendimiento, fecha_inicio, fecha_fin):
    
    productos = productos_controller.get_all(usuario_id, emprendimiento.id_)
    productos_df = pd.DataFrame(productos)

    ventas = ventas_controller.get_all(usuario_id, emprendimiento.id_)
    ventas_range = []
    for venta in ventas:
        if (pd.to_datetime(venta.fecha) >= fecha_inicio) & (pd.to_datetime(venta.fecha) < fecha_fin):
            ventas_range.append(venta)

    if ventas_range != []:
        
        precios = []
        cantidades_ventas = []
        for producto in productos:

            cantidad_ventas = 0
            for venta in ventas_range:
                for linea_venta in venta.lineas_venta:
                    if linea_venta['id_producto'] == producto.id_:
                        cantidad_ventas += linea_venta['cantidad']
            cantidades_ventas.append(cantidad_ventas)
            
            precio_producto = productos_controller.get_last_precio(producto, usuario_id, emprendimiento.id_)
            precios.append(precio_producto.precio)
        
        productos_df['total'] = np.array(precios) * np.array(cantidades_ventas) / 1.5
        productos_df['ventas'] = cantidades_ventas
        productos_df['porcentaje'] = productos_df['total'] / productos_df['total'].sum()
        sorted_total_productos_df = productos_df.sort_values(by="total", ascending=False)
        sorted_ventas_productos_df = productos_df.sort_values(by="ventas", ascending=False)

        plot_top_total(sorted_total_productos_df[:5])
        plot_top_ventas(sorted_ventas_productos_df[:5])

        return render_template("emprendimientos/informes/informe_productos_global.html", 
                            emprendimiento=emprendimiento,
                            fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                            fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'))
    else:
        flash('No hay ventas de productos registradas para este período')
        return redirect(url_for('views.informes_views.informes'))

################################################################################################

def plot_sales(df):
    plt.figure(figsize=(16, 3))
    plt.plot(df.index, df['ventas'])
    plt.xticks(df.index[::2], rotation=30)
    plt.ylabel('Cantidad de ventas')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/productos_ventas.png', bbox_inches='tight')

def plot_stock(df):
    diff = np.diff(df['ventas'], prepend=True)
    diff[diff < 0] = 0
    plt.figure(figsize=(16, 3))
    plt.plot(df.index, diff)
    plt.ylabel('Cantidad de stock')
    plt.xticks(df.index[::4], rotation=30)
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/productos_stock.png', bbox_inches='tight')

################################################

def informe_producto_ingresado(usuario_id, emprendimiento, fecha_inicio, fecha_fin, producto_ingresado):

    ventas = ventas_controller.get_all(usuario_id, emprendimiento.id_)
    ventas_range = []
    for venta in ventas:
        if (pd.to_datetime(venta.fecha) >= fecha_inicio) & (pd.to_datetime(venta.fecha) < fecha_fin):
            ventas_range.append(venta)

    if ventas_range != []:
        
        ###### Ventas del producto ingresado ############
        fechas = []
        cantidades = []
        clientes = []
        for venta in ventas_range:
            for linea_venta in venta.lineas_venta:
                if linea_venta['id_producto'] == producto_ingresado.id_:
                    fechas.append(venta.fecha)
                    cantidades.append(linea_venta['cantidad'])
                    if venta.dni_cliente not in clientes:
                        clientes.append(venta.dni_cliente)

        if fechas != []:
            ventas_producto_df = pd.DataFrame(cantidades, index=fechas, columns=['ventas'])
            ventas_producto_df.index = pd.to_datetime(ventas_producto_df.index)
            ventas_producto_df.index.name = 'fecha'
            ventas_producto_df = ventas_producto_df.groupby('fecha').sum()
            plot_sales(ventas_producto_df)
            no_ventas = False

            ############ Stock del producto ingresado ############
            pedidos = pedidos_controller.get_all(usuario_id, emprendimiento.id_)
            fechas = []
            cantidades = []
            insumos_id = [linea_insumo['id_insumo'] for linea_insumo in producto_ingresado.lineas_insumo]
            for pedido in pedidos:
                for linea_pedido in pedido.lineas_pedido:
                    if linea_pedido['id_articulo'] in insumos_id:
                        fechas.append(pedido.fecha_recepcion)
                        cantidades.append(linea_pedido['cantidad'])

            pedidos_producto_df = pd.DataFrame(cantidades, index=fechas, columns=['ventas'])
            pedidos_producto_df.index = pd.to_datetime(pedidos_producto_df.index)
            pedidos_producto_df.index.name = 'fecha'
            pedidos_producto_df = pedidos_producto_df.groupby('fecha').sum()

            ventas_producto_df['ventas'] = -ventas_producto_df['ventas'] 
            stock_producto_df = ventas_producto_df.append(pedidos_producto_df)
            stock_producto_df.sort_index(inplace=True)

            plot_stock(stock_producto_df)

            ###### KPIs del producto ingresado ######
            cantidad_clientes = len(clientes)
            
            costo_gastado = pedidos_producto_df['ventas'].sum() * producto_ingresado.costo
            ganancia_obtenida = (-ventas_producto_df['ventas']).sum() * producto_ingresado.costo * emprendimiento.margen_ganancia
            rendimiento = ganancia_obtenida / costo_gastado

            promedio_dias_ventas = ventas_producto_df.index.to_series().diff().mean().days

        else:
            cantidad_clientes = 0
            rendimiento = 0
            promedio_dias_ventas = 0
            no_ventas = True
        
        return render_template("emprendimientos/informes/informe_productos.html", 
                            emprendimiento=emprendimiento,
                            fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                            fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'),
                            producto=producto_ingresado,
                            cantidad_clientes=cantidad_clientes,
                            rendimiento=rendimiento,
                            promedio_dias_ventas=promedio_dias_ventas,
                            no_ventas=no_ventas)

    else:
        flash('No hay ventas registradas para este período')
        return redirect(url_for('views.informes_views.informes'))