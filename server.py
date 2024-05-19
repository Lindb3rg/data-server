from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/telemetry', methods=['POST'])
def receive_data():
    
    data = request.json.get('data')
    print(data)
    if data:
        response = requests.post("http://localhost:5001/predict", json={'data': data}, timeout=5)
        if response.status_code == 200:
            print(({'message': 'Data received successfully'}), 200)
            prediction = response.json().get('prediction')
            return jsonify({'message': 'Data received and processed', 'prediction': prediction}), 200
        else:
            return jsonify({'message': 'Failed to get prediction from ML model'}), response.status_code
        
    
    return jsonify({'message': 'No data received'}), 400


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
        





