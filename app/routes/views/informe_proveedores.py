from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from ...controllers import pedidos_controller, proveedores_controller, emprendimientos_controller, productos_controller, insumos_controller
from ...models.models import Emprendimiento, Proveedor

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns

############

def plot_pedidos(df):
    plt.figure(figsize=(16, 3))
    plt.plot(df.index, df['cantidad'])
    if len(df.index) > 10:
        plt.xticks(df.index[::2], rotation=30)
    else:
        plt.xticks(df.index, rotation=30)
    plt.ylabel('Cantidad de productos')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/proveedores_pedidos.png', bbox_inches='tight')
    
############

informe_proveedores_scope = Blueprint('informe_proveedores', __name__, url_prefix='/informe_proveedores')

@informe_proveedores_scope.post("/informe_proveedores")
def informe_proveedores():

    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    data = request.form
    fecha_inicio = pd.to_datetime(data['fecha_inicio'])
    fecha_fin = pd.to_datetime(data['fecha_fin'])
    
    proveedor_id = data['proveedor_id']

    if proveedor_id is not None:

        proveedor_ = Proveedor(id_=proveedor_id)
        proveedor_ingresado = proveedores_controller.get_by_id(proveedor_, usuario_id, emprendimiento_id)
        
        pedidos = pedidos_controller.get_by_proveedor(usuario_id, emprendimiento_id, proveedor_ingresado.id_)
        pedidos_range = []
        for pedido in pedidos:
            if (pd.to_datetime(pedido.fecha_confeccion) >= fecha_inicio) & (pd.to_datetime(pedido.fecha_confeccion) < fecha_fin):
                pedidos_range.append(pedido)

        if pedidos_range != []:
            
            fechas_confeccion = []
            fechas_recepcion = []
            cantidad_productos = []
            pedidos_cancelados = 0
            for pedido in pedidos_range:
                fechas_confeccion.append(pedido.fecha_confeccion)
                if pedido.fecha_recepcion is not None:
                    fechas_recepcion.append(pedido.fecha_recepcion)
                    cantidad_productos.append(len(pedido.lineas_pedido))
                if pedido.estado == 'cancelado':
                    pedidos_cancelados += 1
                
            pedidos_df = pd.DataFrame(cantidad_productos, columns=['cantidad'], index=pd.to_datetime(fechas_recepcion))
            pedidos_df.sort_index(inplace=True)
            plot_pedidos(pedidos_df)

            proveedores_tasa_cancelacion = pedidos_cancelados / len(pedidos_range) * 100
            tiempo_demora = pedidos_df.index.to_series().diff().mean().days
            
            frecuencia_compra = pd.to_datetime(fechas_confeccion).to_series().sort_values(0).diff().mean().days
            
            productos = productos_controller.get_all(usuario_id, emprendimiento_id)
            insumos = insumos_controller.get_all(usuario_id, emprendimiento_id)
            productos_proveedor = proveedores_controller.get_articulos(proveedor_ingresado, usuario_id, emprendimiento_id)
            porcentaje_productos = len(productos_proveedor) / (len(productos) + len(insumos))
            no_pedidos = False
        else:
            proveedores_tasa_cancelacion = 0
            frecuencia_compra = 0
            porcentaje_productos = 0
            tiempo_demora = 0
            no_pedidos = True
        
        return render_template("emprendimientos/informes/informe_proveedores.html", 
                            emprendimiento=emprendimiento,
                            fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                            fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'),
                            proveedor=proveedor_ingresado,
                            proveedores_tasa_cancelacion=proveedores_tasa_cancelacion,
                            frecuencia_compra=frecuencia_compra,
                            porcentaje_productos=porcentaje_productos,
                            tiempo_demora=tiempo_demora,
                            no_pedidos=no_pedidos)

    else:
        flash('Debe seleccionar un proveedor')
        return redirect(url_for('views.informes_views.informes'))
