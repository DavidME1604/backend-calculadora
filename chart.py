import numpy as np
import matplotlib.pyplot as plt
from flask import url_for


# Definir la función que genera otra función
def f(v0, interes, a):
    def funcion(x):
        return v0 * (1 + interes) ** x + a * (((1 + interes) ** x - (1 + interes)) / interes)
    return funcion

import os

def graficar(capitalInicial, aporte, interes,frequency):
    funcion_reemplazada = f(capitalInicial, interes, aporte)
    x = np.linspace(1, periodo(frequency), 60)
    y = funcion_reemplazada(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title('Gráfica interés vs Ganancia', fontsize=16)
    plt.xlabel('Interés', fontsize=14)
    plt.ylabel('Ganancia', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    image_path = os.path.join(os.getcwd(), 'static', 'grafico_funcion.png')
    plt.savefig(image_path, format='png', dpi=300, bbox_inches='tight')
    plt.close()

    # Verificar si el archivo fue creado
    if os.path.exists(image_path):
        print(f"Archivo generado en: {image_path}, Tamaño: {os.path.getsize(image_path)} bytes")
        image_url = url_for('static', filename='grafico_funcion.png', _external=True)
        print('La url es: {}'.format(image_url))
    else:
        print("No se pudo generar el archivo.")

def periodo(frequency):
    if frequency == 'diario':
        return 365
    elif frequency == 'mensual':
        return 12
    elif frequency == 'semanal':
        return 52
    elif frequency == 'trimestral':
        return 4
    elif frequency == 'semestral':
        return 2
    elif frequency == 'anual':
        return 1
    else:
        return None


def table_data(initial_capital, num_periods, periodic_contribution, interest, start_period=1, frequency=None):
    """
    Genera datos para la tabla con base en el capital inicial, los períodos,
    el aporte periódico, y la tasa de interés.
    """
    table_data = []
    for period in range(start_period, start_period + num_periods):
        # Cálculo del total usando la fórmula original
        if abs(interest) < 1e-10:  # Evitar división por cero en tasas muy pequeñas
            total = initial_capital + periodic_contribution * period
        else:
            total = (initial_capital * (1 + interest) ** period +
                     periodic_contribution * (((1 + interest) ** period - (1 + interest)) / interest))

        # Ganancia como la diferencia entre Total y el Capital Inicial
        gain = total - initial_capital

        # Agregar datos a la tabla
        table_data.append({
            'period': period,
            'contribution': periodic_contribution,
            'capital': round(initial_capital, 2),
            'gain': round(gain, 2),
            'total': round(total, 2),
        })

    return table_data











