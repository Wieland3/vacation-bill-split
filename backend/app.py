from flask import Flask, send_from_directory, request, jsonify
import json

app = Flask(__name__, static_folder="../frontend/vue-project/dist")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/assets/<path:filename>')
def serve_js(filename):
    return send_from_directory(app.static_folder + '/assets', filename)


@app.route('/send-cash', methods=['POST'])
def send_cash():
    data = request.get_json()
    with open("./backend/data/data.json", "r") as json_file:
        json_data = json_file.read()
    json_data = json.loads(json_data)
    name = data['name']
    current = float(json_data[name])
    amount = float(data['price'])
    current += amount
    json_data[name] = current
    with open("./backend/data/data.json", "w") as json_file:
        json.dump(json_data, json_file)
    return jsonify({'status': 'success'}), 200


@app.route('/get-cash', methods=['GET'])
def get_amount():
    with open("./backend/data/data.json", "r") as json_file:
        json_data = json_file.read()
    json_data = json.loads(json_data)
    amount = 0
    for key in json_data:
        amount += float(json_data[key])
    return jsonify({'amount': amount}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
