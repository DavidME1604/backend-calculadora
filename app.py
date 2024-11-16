from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from interes import obtener_interes
from chart import graficar

app = Flask(__name__)
CORS(app)


main_data = {}

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json

    initial_capital = data.get('initialCapital', 0)
    final_capital = data.get('finalCapital', 0)
    num_periods = data.get('numPeriods', 0)
    periodic_contribution = data.get('periodicContribution', 0)
    main_data['initialCapital'] = initial_capital
    main_data['finalCapital'] = final_capital
    main_data['numPeriods'] = num_periods
    main_data['periodicContribution'] = periodic_contribution
    result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)
    main_data['interes'] = result
    return jsonify({'result': result})

@app.route('/api/chart', methods=['POST'])
def chart():
    initial_capital = main_data.get('initialCapital', 0)
    periodic_contribution = main_data.get('periodicContribution', 0)
    interes = main_data.get('interes', 0)
    graficar(initial_capital, periodic_contribution, interes)
    image_url = url_for('static', filename='grafico_funcion.png', _external=True)
    return jsonify({"chartUrl": image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
