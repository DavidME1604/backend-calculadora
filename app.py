from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution):
    # Ejemplo de cálculo de interés (ajusta según tu fórmula)
    if num_periods == 0:
        return "Número de períodos no puede ser cero"

    interest_rate = ((final_capital - initial_capital - (periodic_contribution * num_periods)) / (
                initial_capital * num_periods)) * 100
    return interest_rate


@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json

    initial_capital = data.get('initialCapital', 0)
    final_capital = data.get('finalCapital', 0)
    num_periods = data.get('numPeriods', 0)
    periodic_contribution = data.get('periodicContribution', 0)

    result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
