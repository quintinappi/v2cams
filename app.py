from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# This will store the license plates and timestamps
data_list = []

@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        # Extract the license plate and timestamp from the data
        # The exact keys will depend on the structure of your JSON data
        license_plate = data['license_plate']
        timestamp = data['timestamp']
        # Add the details to the start of the list
        data_list.insert(0, (license_plate, timestamp))
        return jsonify({'message': 'Data received successfully!'}), 200
    except Exception as e:
        return jsonify({'message': 'Invalid JSON payload', 'error': str(e)}), 400

@app.route('/')
def home():
    # Generate an HTML string with the license plates and timestamps
    html = '<html><body><ul>'
    for license_plate, timestamp in data_list:
        html += f'<li>{timestamp}: {license_plate}</li>'
    html += '</ul></body></html>'
    return html

if __name__ == '__main__':
    app.run(debug=True)