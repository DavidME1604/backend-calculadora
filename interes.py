from scipy import optimize

def f(v0, vf, n, a):
    def funcion(x):
        if abs(x) < 1e-10:
            return vf - v0 * (1 + x) ** n
        else:
            return vf - v0 * (1 + x) ** n - a * (((1 + x) ** n - (1 + x)) / x)

    return funcion

def obtener_interes(capital_inicial, capital_final, numero_periodos, aporte):
    return optimize.newton(f(capital_inicial, capital_final, numero_periodos, aporte), 1e-5)
