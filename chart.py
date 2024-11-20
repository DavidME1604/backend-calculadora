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


def table_data(initial_capital, num_periods, periodic_contribution, interest):
    table_data = []
    capital = initial_capital
    funcion_reemplazada = f(initial_capital, interest, periodic_contribution)
    for i in range(1, num_periods + 1):
        if i == 1:
            table_data.append({
                'period': i,
                'contribution': periodic_contribution,
                'capital': round(capital, 2),
                'gain': round(funcion_reemplazada(1) - initial_capital, 2),
                'total': round(funcion_reemplazada(1), 2)
            })
        else:
            capital = funcion_reemplazada(i - 1)
            total = funcion_reemplazada(i)
            table_data.append({
                'period': i,
                'contribution': periodic_contribution,
                'capital': round(capital, 2),
                'gain': round(total - capital - periodic_contribution, 2),
                'total': round(total, 2)
            })
    return table_data
