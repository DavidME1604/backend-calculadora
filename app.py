from flask import Flask, request, jsonify
from flask_cors import CORS
from interes import obtener_interes


app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hola, Render!"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    input_values = data.get('input', 0)
    result = obtener_interes(input_values['initialCapital'],input_values['finalCapital'],input_values['numPeriods'],input_values['periodicContribution'],)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
