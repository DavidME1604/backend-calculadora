from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hola, Render!"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    input_value = data.get('input', 0)
    result = input_value * 2  # Ejemplo de cálculo simple
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
