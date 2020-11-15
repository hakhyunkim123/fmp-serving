from flask import Flask
from serving import serving_bp

app = Flask(__name__)
app.register_blueprint(serving_bp)

if __name__ == '__main__':
    # 에러코드집 캐싱
    app.run(host='0.0.0.0', port='8000')
