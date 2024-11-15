from flask import Flask, request, jsonify
from flask_cors import CORS
from interes import obtener_interes

app = Flask(__name__)
CORS(app)


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
