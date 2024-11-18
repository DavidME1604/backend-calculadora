from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from interes import obtener_interes
from chart import graficar

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        initial_capital = float(data.get('initialCapital', 0))
        final_capital = float(data.get('finalCapital', 0))
        num_periods = float(data.get('numPeriods', 0))
        periodic_contribution = float(data.get('periodicContribution', 0))
        contribution_period = data.get('contributionPeriod', 'semanal')
        interest_display = data.get('interestDisplay', 'semanal')

        if initial_capital < 0 or final_capital < 0 or num_periods <= 0 or periodic_contribution < 0:
            return jsonify({'error': 'Los valores ingresados deben ser positivos.'}), 400

        # Ajuste de períodos y aportes
        if interest_display == 'semanal' and contribution_period == 'mensual':
            num_periods /= 4.33
        elif interest_display == 'semanal' and contribution_period == 'anual':
            num_periods /= 52
        elif interest_display == 'mensual' and contribution_period == 'semanal':
            num_periods *= 4.33
        elif interest_display == 'mensual' and contribution_period == 'anual':
            num_periods /= 12
        elif interest_display == 'anual' and contribution_period == 'semanal':
            num_periods *= 52
        elif interest_display == 'anual' and contribution_period == 'mensual':
            num_periods *= 12

        if contribution_period == 'mensual' and interest_display == 'semanal':
            periodic_contribution /= 4.33
        elif contribution_period == 'anual' and interest_display == 'semanal':
            periodic_contribution /= 52
        elif contribution_period == 'anual' and interest_display == 'mensual':
            periodic_contribution /= 12

        # Calcular interés compuesto
        result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)
        print(f"Interés compuesto calculado: {result}")

        # Generar gráfica
        chart_url = graficar(initial_capital, periodic_contribution, result)
        print(f"Gráfica generada: {chart_url}")

        # Respuesta al frontend
        return jsonify({
            'result': result,
            'initialCapital': initial_capital,
            'periodicContribution': periodic_contribution,
            'interestRate': result,
            'chartUrl': chart_url  # URL de la gráfica
        })

    except Exception as e:
        print(f"Error en /api/calculate: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500
