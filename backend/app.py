from flask import Flask, send_from_directory, request, jsonify

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
    print(data)
    return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
