from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.models.exceptions import NoEntitiesRegistered
from ...controllers import ventas_controller, emprendimientos_controller
from ...models.models import Emprendimiento

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns

from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from statsmodels.tsa.api import Holt

#################

def mean_min_max(df):
    monto_mean = df['monto'].mean()
    monto_min = df[df['monto'] != 0]['monto'].min()
    monto_max = df['monto'].max()

    ventas_mean = df['ventas'].mean()
    ventas_min = df[df['ventas'] != 0]['ventas'].min()
    ventas_max = df['ventas'].max()
    
    monto = {'mean': int(monto_mean), 'min': int(monto_min), 'max': int(monto_max)}
    ventas = {'mean': int(ventas_mean), 'min': int(ventas_min), 'max': int(ventas_max)}

    return monto, ventas

def plot_daily_df(df):

    fig, axes = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

    axes[0].step(df.index, df['ventas'], where='pre')
    axes[1].step(df.index, df['monto'], where='pre')
    
    plt.xticks(df.index[::2], rotation=45)
    
    axes[0].set_ylabel('Cantidad clientes')
    axes[0].set_title('Clientes')
    axes[1].set_ylabel('Monto ($)')
    axes[1].set_title('Monto Vendido')


    
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/ventas_daily.png', bbox_inches='tight')

def plot_weekly_df(df):

    fig, axes = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

    axes[0].step(df.index, df['ventas'], marker='o', markersize=7, markerfacecolor='black')
    axes[1].step(df.index, df['monto'], marker='o', markersize=7, markerfacecolor='black')
    
    plt.xticks(df.index, rotation=45)

    axes[0].set_ylabel('Cantidad clientes')
    axes[0].set_title('Clientes')
    axes[1].set_ylabel('Monto ($)')
    axes[1].set_title('Monto Vendido')
    
    
    
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/ventas_weekly.png', bbox_inches='tight')

def plot_monthly_df(df):

    fig, axes = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

    month_labels = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    months = list(map(lambda x: month_labels[x], list(df.index.month)))

    sns.barplot(x=months, y=df['monto'], ax=axes[0])
    sns.barplot(x=months, y=df['ventas'], ax=axes[1])
    
    axes[0].set_title('Clientes')
    axes[0].set_ylabel('Cantidad clientes')
    axes[1].set_title('Monto Vendido')
    axes[1].set_ylabel('Monto ($)')
    
    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/ventas_monthly.png', bbox_inches='tight')

def trend(df):
    fig, axes = plt.subplots(2, 1, figsize=(13, 5), sharex=True)

    trend = seasonal_decompose(df['ventas'], model='add').trend
    axes[0].plot(trend.index, trend, color='darkcyan')

    trend = seasonal_decompose(df['monto'], model='add').trend
    axes[1].plot(trend.index, trend, color='firebrick')

    plt.xticks(trend.index[::2], rotation=45)

    axes[0].set_ylabel('Cantidad clientes')
    axes[0].set_title('Clientes')
    axes[1].set_ylabel('Monto ($)')
    axes[1].set_title('Monto Vendido')

    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/ventas_trend.png', bbox_inches='tight')

def forecast(df):
    model = Holt(df['ventas'], initialization_method="estimated")
    results = model.fit(smoothing_level=0.8, smoothing_trend=0.05, optimized=False)

    sales_predicted = df['ventas'].append(results.forecast(60))
    sales_predicted = sales_predicted[len(df['ventas']):] 
    sales_predicted += np.random.normal(0, 1, len(sales_predicted))

    upper_CIs = []
    lower_CIs = []
    for i in range(len(sales_predicted)):
        upper_CIs.append(sales_predicted[i] + 0.1*i)
        lower_CIs.append(sales_predicted[i] - 0.1*i)
    sales_upper_CIs = np.array(upper_CIs)
    sales_lower_CIs = np.array(lower_CIs)
    sales_upper_CIs[sales_upper_CIs < 0] = 0
    sales_lower_CIs[sales_lower_CIs < 0] = 0

    ###

    model = Holt(df['monto'], initialization_method="estimated")
    results = model.fit(smoothing_level=0.8, smoothing_trend=0.05, optimized=False)

    monto_predicted = df['monto'].append(results.forecast(60))
    monto_predicted = monto_predicted[len(df['ventas']):] 
    monto_predicted += np.random.normal(0, 500, len(monto_predicted))

    upper_CIs = []
    lower_CIs = []
    for i in range(len(monto_predicted)):
        upper_CIs.append(monto_predicted[i] + 100*i)
        lower_CIs.append(monto_predicted[i] - 100*i)
    monto_upper_CIs = np.array(upper_CIs)
    monto_lower_CIs = np.array(lower_CIs)
    monto_upper_CIs[monto_upper_CIs < 0] = 0
    monto_lower_CIs[monto_lower_CIs < 0] = 0

    ###

    fig, axes = plt.subplots(2, 1, figsize=(13, 5), sharex=True)

    axes[0].plot(df['ventas'], label='Datos')
    axes[0].plot(sales_predicted, label='Pronóstico')
    axes[0].fill_between(sales_predicted.index, sales_upper_CIs, sales_lower_CIs, color='silver')
    axes[0].legend(loc='upper left')

    axes[1].plot(df['monto'])
    axes[1].plot(monto_predicted)
    axes[1].fill_between(sales_predicted.index, monto_upper_CIs, monto_lower_CIs, color='silver')

    index = df['ventas'].index.append(sales_predicted.index)
    plt.xticks(index[::4], rotation=45)

    axes[0].set_ylabel('Cantidad clientes')
    axes[0].set_title('Clientes')
    axes[1].set_ylabel('Monto ($)')
    axes[1].set_title('Monto Vendido')

    plt.tight_layout()
    plt.savefig('app/views/static/images/informes/ventas_forecast.png', bbox_inches='tight')

#################

informe_ventas_scope = Blueprint('informe_ventas', __name__, url_prefix='/informe_ventas')

@informe_ventas_scope.post("/informe_ventas")
def informe_ventas():

    data = request.form
    fecha_inicio = pd.to_datetime(data['fecha_inicio'])
    fecha_fin = pd.to_datetime(data['fecha_fin'])
    
    usuario_id = request.cookies.get('usuario_id')
    emprendimiento_id = request.cookies.get('emprendimiento_id')
    emprendimiento_ = Emprendimiento(id_=emprendimiento_id)
    emprendimiento = emprendimientos_controller.get_by_id(emprendimiento_, usuario_id)

    # Ventas
    try: 
        ventas = ventas_controller.get_all(usuario_id, emprendimiento_id)
    except NoEntitiesRegistered:
        flash('No hay ventas registradas')
        return redirect(url_for('views.informes_views.informes'))

    ventas_df = pd.DataFrame(ventas)
    ventas_df['fecha'] = pd.to_datetime(ventas_df['fecha'])
    ventas_df = ventas_df.groupby('fecha')['total'].agg(['sum','count']).rename(columns={'sum':'monto', 'count':'ventas'})
    ventas_df.sort_index(inplace=True)
    
    # Mask between dates
    mask = (ventas_df.index >= fecha_inicio) & (ventas_df.index < fecha_fin)
    ventas_range = ventas_df[mask]

    if not ventas_range.empty:

        # GLOBAL
        ganancia_bruta, total_ventas = ventas_range.sum()
        ganancia_neta = int(ganancia_bruta/emprendimiento.margen_ganancia)
        global_ = {'ganancia_bruta': ganancia_bruta, 'total_ventas': total_ventas, 'ganancia_neta': ganancia_neta}

        # Ventas frequencies
        ventas_daily = ventas_range
        daily_monto, daily_ventas = mean_min_max(ventas_daily)

        ventas_weekly = ventas_daily.resample('W-Mon').sum()
        weekly_monto, weekly_ventas = mean_min_max(ventas_weekly)
        
        ventas_monthly = ventas_daily.resample('M').sum()
        monthly_monto, monthly_ventas = mean_min_max(ventas_monthly)

        plot_daily_df(ventas_daily)
        plot_weekly_df(ventas_weekly)
        plot_monthly_df(ventas_monthly)

        trend(ventas_df)
        forecast(ventas_df)
        
        return render_template("emprendimientos/informes/informe_ventas.html",
                                global_=global_,
                                emprendimiento=emprendimiento,
                                fecha_inicio=datetime.strftime(fecha_inicio, '%d/%m/%Y'),
                                fecha_fin=datetime.strftime(fecha_fin, '%d/%m/%Y'),
                                daily_monto=daily_monto,
                                daily_ventas=daily_ventas,
                                weekly_monto=weekly_monto,
                                weekly_ventas=weekly_ventas,
                                monthly_monto=monthly_monto,
                                monthly_ventas=monthly_ventas)

    else:
        flash('No hay ventas registradas para este período')
        return redirect(url_for('views.informes_views.informes'))