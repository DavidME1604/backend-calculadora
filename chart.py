import numpy as np
import matplotlib.pyplot as plt
from flask import url_for


# Definir la función que genera otra función
def f(v0, interes, a):
    def funcion(x):
        return v0 * (1 + interes) ** x + a * (((1 + interes) ** x - (1 + interes)) / interes)
    return funcion

def graficar(capitalInicial, aporte, interes):

    funcion_reemplazada = f(capitalInicial, interes, aporte)
    x = np.linspace(1, 12, 60)

    y = funcion_reemplazada(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2, label=r'$f(x) = 100 \cdot (1 + 0.0015)^x + 5 \cdot \frac{(1 + 0.0015)^x - (1 + 0.0015)}{0.0015}$')

    plt.title('Gráfica de la Función Generada', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('grafico_funcion', format='png', dpi=300, bbox_inches='tight')

    plt.show()

graficar(100, 5, 0.0015)
