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
        contribution_period = data.get('frequency')
        if initial_capital < 0 or final_capital < 0 or num_periods <= 0 or periodic_contribution < 0:
            return jsonify({'error': 'Los valores ingresados deben ser positivos.'}), 400
        result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)
        graficar(initial_capital, periodic_contribution, result)
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error en /api/calculate: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500