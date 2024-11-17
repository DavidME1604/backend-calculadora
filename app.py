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

        # Calcular interés
        result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)

        if contribution_period == 'mensual' and interest_display == 'semanal':
            result /= 4.33
        elif contribution_period == 'anual' and interest_display == 'semanal':
            result /= 52
        elif contribution_period == 'anual' and interest_display == 'mensual':
            result /= 12

        graficar(initial_capital, periodic_contribution, result)
        return jsonify({'result': result})

    except Exception as e:
        print(f"Error en /api/calculate: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500

@app.route('/api/chart', methods=['POST'])
def chart():
    image_url = url_for('static', filename='grafico_funcion.png', _external=True)
    print('La url es: {}'.format(image_url))
    return jsonify({"chartUrl": image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
