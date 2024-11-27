from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from interes import obtener_interes
from chart import graficar, table_data

app = Flask(__name__)
CORS(app)

initial_capital = 0
final_capital = 0
num_periods = 0
periodic_contribution = 0
interest = 0

@app.route('/api/calculate', methods=['POST'])
def calculate():
    global initial_capital, final_capital, num_periods, periodic_contribution, interest  # Indicar que se va a modificar la variable global
    data = request.json
    try:
        initial_capital = float(data.get('initialCapital', 0))
        final_capital = float(data.get('finalCapital', 0))
        num_periods = int(data.get('numPeriods', 0))
        periodic_contribution = float(data.get('periodicContribution', 0))
        frequency = str(data.get('frequency', 0))

        if initial_capital < 0 or final_capital < 0 or num_periods <= 0 or periodic_contribution < 0:
            return jsonify({'error': 'Los valores ingresados deben ser positivos.'}), 400
        interest = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)
        graficar(initial_capital, periodic_contribution, interest,frequency)

        return jsonify({'result': interest})
    except Exception as e:
        print(f"Error en /api/calculate: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500

@app.route('/api/chart', methods=['POST'])
def chart():
    image_url = url_for('static', filename='grafico_funcion.png', _external=True)
    print('La url es: {}'.format(image_url))
    return jsonify({"chartUrl": image_url})

@app.route('/api/table', methods=['POST'])
def table():
    global initial_capital, final_capital, num_periods, periodic_contribution, interest
    try:
        data = request.json
        required_rows = int(data.get('requiredRows', 5))
        data_table = table_data(initial_capital, required_rows, periodic_contribution, interest)

        return jsonify({'dataTable': data_table})
    except Exception as e:
        print(f"Error en /api/table: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
