from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Python App running with Docker and GitHub Actions!</h1>"

@app.route('/health')
def health():
    return jsonify({
        "status": "success",
        "message": "App is healthy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
