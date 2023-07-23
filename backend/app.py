from flask import Flask, send_from_directory, request, jsonify
import json
import os

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(get_base_dir() + "/frontend/vue-project/dist", 'index.html')


@app.route('/assets/<path:filename>')
def serve_js(filename):
    return send_from_directory(get_base_dir() + "/frontend/vue-project/dist/assets", filename)


@app.route('/send-cash', methods=['POST'])
def send_cash():
    data = request.get_json()
    json_data = get_json_data()
    name = data['name']
    current = float(json_data[name])
    amount = float(data['price'])
    current += amount
    json_data[name] = current
    with open(get_base_dir() + "/backend/data/data.json", "w") as json_file:
        json.dump(json_data, json_file)
    return jsonify({'status': 'success'}), 200


@app.route('/get-cash', methods=['GET'])
def get_amount():
    json_data = get_json_data()
    amount = 0
    for key in json_data:
        amount += float(json_data[key])
    return jsonify({'amount': amount}), 200


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__)) + "/.."


def get_json_data():
    # check if file exists and if not create it
    if not os.path.exists(get_base_dir() + "/backend/data/data.json"):
        with open(get_base_dir() + "/backend/data/data.json", "w") as json_file:
            json.dump({"Jan": 0.0, "Felix": 0.0, "Wieland": 0.0}, json_file)

    # read the file
    with open(get_base_dir() + "/backend/data/data.json", "r") as json_file:
        json_data = json_file.read()
    json_data = json.loads(json_data)
    return json_data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
