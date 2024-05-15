
from flask import Flask, request, jsonify

app = Flask(__name__)
telemetry_data = []

@app.route('/metrics', methods=['POST'])
def receive_telemetry():
    data = request.get_json()
    telemetry_data.append(data)
    return jsonify({"message": "Data received"}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(telemetry_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)