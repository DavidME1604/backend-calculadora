from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from interes import obtener_interes
from chart import graficar, table_data

app = Flask(__name__)
CORS(app)

data_table = []

@app.route('/api/calculate', methods=['POST'])
def calculate():
    global data_table  # Indicar que se va a modificar la variable global
    data = request.json
    print(f"Datos recibidos: {data}")
    try:
        initial_capital = float(data.get('initialCapital', 0))
        final_capital = float(data.get('finalCapital', 0))
        num_periods = int(data.get('numPeriods', 0))
        periodic_contribution = float(data.get('periodicContribution', 0))
        frequency = str(data.get('frequency', 0))
        print(frequency)

        if initial_capital < 0 or final_capital < 0 or num_periods <= 0 or periodic_contribution < 0:
            return jsonify({'error': 'Los valores ingresados deben ser positivos.'}), 400
        result = obtener_interes(initial_capital, final_capital, num_periods, periodic_contribution)
        graficar(initial_capital, periodic_contribution, result,frequency)

        # Actualizar la tabla global con nuevos cálculos
        data_table = table_data(initial_capital, num_periods, periodic_contribution, result)

        return jsonify({'result': result})
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
    try:
        data = request.json
        required_rows = int(data.get('requiredRows', 5))
        global data_table

        if not data_table:
            return jsonify({'error': 'No hay datos calculados. Por favor, realiza un cálculo primero.'}), 400

        if required_rows > len(data_table):
            last_row = data_table[-1]
            initial_capital = last_row['capital']
            periodic_contribution = last_row['contribution']
            interest = 0.20171  # Ejemplo: tasa de interés fija
            last_period = last_row['period']
            additional_data = table_data(
                initial_capital,
                required_rows - len(data_table),
                periodic_contribution,
                interest,
                start_period=last_period + 1
            )
            data_table.extend(additional_data)

        return jsonify({'dataTable': data_table[:required_rows]})
    except Exception as e:
        print(f"Error en /api/table: {e}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
