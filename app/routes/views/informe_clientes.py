from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from ...controllers import ventas_controller, clientes_controller, emprendimientos_controller
from ...models.models import Emprendimiento, Cliente

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns

informe_clientes_scope = Blueprint('informe_clientes', __name__, url_prefix='/informe_clientes')
@informe_clientes_scope.post("/informe_clientes_dispatcher")
def informe_clientes_dispatcher():
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    data = request.form
    fecha_inicio = pd.to_datetime(data['fecha_inicio'])
    fecha_fin = pd.to_datetime(data['fecha_fin'])
    
    cliente_id = request.form.get('cliente_id')
    cliente_ = Cliente(id_=cliente_id)
    cliente_ingresado = clientes_controller.get_by_id(cliente_, usuario_id, emprendimiento_id)
    
    if request.form['action'] == 'global':
        return informe_global(usuario_id, emprendimiento, fecha_inicio, fecha_fin)
    elif request.form['action'] == 'cliente_ingresado':
        if cliente_id is not None:
            return informe_cliente_ingresado(usuario_id, emprendimiento, fecha_inicio, fecha_fin, cliente_ingresado)
        else:
            flash('Debe seleccionar un cliente')
            return redirect(url_for('views.informes_views.informes'))
    else:
        raise ValueError("Proveedor received an invalid method")

################################################

def plot_top_total(df):
    
    plt.figure(figsize=(16, 3))
    sns.barplot(x=df['total'], y=df['nombre'])
    plt.ylabel('')
    plt.xlabel('Monto total')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/clientes_ranking_ganancia.png', bbox_inches='tight')

def plot_top_compras(df):
    plt.figure(figsize=(16, 3))
    sns.barplot(x=df['compras'], y=df['nombre'])
    plt.ylabel('')
    plt.xlabel('Cantidad de compras')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/clientes_ranking_cantidad.png', bbox_inches='tight')

################################################

def informe_global(usuario_id, emprendimiento, fecha_inicio, fecha_fin):

    clientes = clientes_controller.get_all(usuario_id, emprendimiento.id_)
    clientes_df = pd.DataFrame(clientes)

    ventas = ventas_controller.get_all(usuario_id, emprendimiento.id_)
    ventas_range = []
    for venta in ventas:
        if (pd.to_datetime(venta.fecha) >= fecha_inicio) & (pd.to_datetime(venta.fecha) < fecha_fin):
            ventas_range.append(venta)

    if ventas_range != []:

        ###### Global: compras y monto total de cada cliente ######
        
        montos = []
        cantidades_compras = []
        for cliente in clientes:
            monto = 0
            cantidad_compras = 0
            for venta in ventas_range:
                if venta.dni_cliente == cliente.dni:
                    monto += venta.total
                    cantidad_compras += len(venta.lineas_venta)
            montos.append(monto)
            cantidades_compras.append(cantidad_compras) 
        
        clientes_df['total'] = np.array(montos) * np.array(cantidades_compras) / 1.5
        clientes_df['compras'] = cantidades_compras
        clientes_df['porcentaje'] = clientes_df['total'] / clientes_df['total'].sum()
        sorted_total_clientes_df = clientes_df.sort_values(by="total", ascending=False)
        sorted_compras_clientes_df = clientes_df.sort_values(by="compras", ascending=False)

        plot_top_total(sorted_total_clientes_df[:5])
        plot_top_compras(sorted_compras_clientes_df[:5])


        ###### Cantidad de clientes nuevos y que regresaron ######
        dnis_anteriores = []
        dnis_actuales = []

        for venta in ventas:
            # Anterior
            if (pd.to_datetime(venta.fecha) < fecha_inicio):
                if venta.dni_cliente not in dnis_anteriores:
                        dnis_anteriores.append(venta.dni_cliente)
            # Actual
            elif (pd.to_datetime(venta.fecha) >= fecha_inicio) & (pd.to_datetime(venta.fecha) < fecha_fin):
                if venta.dni_cliente not in dnis_actuales:
                        dnis_actuales.append(venta.dni_cliente)

        dnis_anteriores = np.array(dnis_anteriores)
        dnis_actuales = np.array(dnis_actuales)
        clientes_nuevos = len(dnis_actuales[np.isin(dnis_actuales, dnis_anteriores, invert=True)])
        clientes_regresaron = len(dnis_actuales[np.isin(dnis_actuales, dnis_anteriores)])


        return render_template("emprendimientos/informes/informe_clientes_global.html", 
                            emprendimiento=emprendimiento,
                            fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                            fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'),
                            clientes_nuevos=clientes_nuevos,
                            clientes_regresaron=clientes_regresaron)

    else:
        flash('No hay ventas registradas para este período')
        return redirect(url_for('views.informes_views.informes'))

################################################

def plot_sales(df):
    plt.figure(figsize=(16, 3))
    plt.plot(df.index, df['compras'])
    if len(df.index) > 10:
        plt.xticks(df.index[::2], rotation=45)
    else:
        plt.xticks(df.index, rotation=45)
    plt.ylabel('Monto comprado ($)')
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/clientes_compras.png', bbox_inches='tight')
    
################################################

def informe_cliente_ingresado(usuario_id, emprendimiento, fecha_inicio, fecha_fin, cliente_ingresado):

    ventas = ventas_controller.get_all(usuario_id, emprendimiento.id_)
    ventas_range = []
    for venta in ventas:
        if (pd.to_datetime(venta.fecha) >= fecha_inicio) & (pd.to_datetime(venta.fecha) < fecha_fin):
            ventas_range.append(venta)

    if ventas_range != []:

        ### COMPRAS DEL CLIENTE
        fechas = []
        montos = []
        monto_total = 0
        for venta in ventas_range:
            monto_total += venta.total
            if venta.dni_cliente == cliente_ingresado.dni:
                fechas.append(venta.fecha)
                montos.append(venta.total)

        if fechas != []:
            compras_cliente_df = pd.DataFrame(montos, index=fechas, columns=['compras'])
            compras_cliente_df.index = pd.to_datetime(compras_cliente_df.index)
            compras_cliente_df.index.name = 'fecha'
            compras_cliente_df = compras_cliente_df.groupby('fecha').sum()
            plot_sales(compras_cliente_df)

            cantidad_compras = len(compras_cliente_df)
            frecuencia_compra = compras_cliente_df.index.to_series().diff().mean().days
            monto_comprado = compras_cliente_df['compras'].sum()
            porcentaje_ventas = monto_comprado / monto_total * 100
            no_cliente = False
        else:
            cantidad_compras = 0
            frecuencia_compra = 0
            monto_comprado = 0
            porcentaje_ventas = 0
            no_cliente = True
            
        return render_template("emprendimientos/informes/informe_clientes.html", 
                            emprendimiento=emprendimiento,
                            fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                            fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'),
                            cliente=cliente_ingresado,
                            cantidad_compras=cantidad_compras,
                            frecuencia_compra=frecuencia_compra,
                            porcentaje_ventas=porcentaje_ventas,
                            monto_comprado=monto_comprado,
                            no_cliente=no_cliente)

    else:
        flash('No hay ventas registradas para este período')
        return redirect(url_for('views.informes_views.informes'))