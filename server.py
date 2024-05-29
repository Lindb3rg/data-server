import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

namespace = os.getenv('namespace', 'unavailable')
chart_name = os.getenv('chart_name', 'unavailable')

@app.route('/telemetry', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    print("This is data from within data-server ",data)
    
    if data:
        try:
            response = requests.post(f"http://{chart_name}-ml-service.{namespace}:5001/predict", json={'data': data})
            response.raise_for_status()
            prediction = response.json().get('prediction')
            print("**********")
            print(f"Machine with ID {namespace} got prediction: {prediction}")
            print("**********")
            return jsonify({'message': 'Data received and processed', 'prediction': prediction}), 200
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return jsonify({'message': 'Failed to get prediction from ML model', 'error': str(http_err)}), response.status_code
        except Exception as err:
            print(f"Other error occurred: {err}")
            return jsonify({'message': 'An error occurred', 'error': str(err)}), 500
    return jsonify({'message': 'No data received'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
