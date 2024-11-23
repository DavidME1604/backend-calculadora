import numpy as np
import matplotlib.pyplot as plt
from flask import url_for


# Definir la función que genera otra función
def f(v0, interes, a):
    def funcion(x):
        return v0 * (1 + interes) ** x + a * (((1 + interes) ** x - (1 + interes)) / interes)
    return funcion

import os

def graficar(capitalInicial, aporte, interes):
    funcion_reemplazada = f(capitalInicial, interes, aporte)
    x = np.linspace(1, 12, 60)
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


def table_data(initial_capital, num_periods, periodic_contribution, interest, start_period=1):
    table_data = []
    for period in range(start_period, start_period + num_periods):
        # Calcular Total usando la fórmula correcta
        total = initial_capital * (1 + interest) ** period

        # Calcular Ganancia como la diferencia entre Total y el Capital Inicial
        gain = total - initial_capital

        # Agregar los datos calculados a la tabla
        table_data.append({
            'period': period,
            'contribution': periodic_contribution,
            'capital': round(initial_capital, 2),  # Capital inicial no cambia en esta fórmula
            'gain': round(gain, 2),
            'total': round(total, 2)
        })

    return table_data




