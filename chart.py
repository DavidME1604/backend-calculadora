import numpy as np
import matplotlib.pyplot as plt


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
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title('Gráfica de la Función Generada', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('static/grafico_funcion.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()
graficar(100, 5, 0.0015)
