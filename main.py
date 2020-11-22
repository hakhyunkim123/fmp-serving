from flask import Flask
from serving import serving_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(serving_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
