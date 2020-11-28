from flask import Flask
from serving import serving_bp
from account_web import account_bp
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'super secret key'
app.register_blueprint(serving_bp)
app.register_blueprint(account_bp)

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
