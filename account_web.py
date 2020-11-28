from flask import request, Blueprint, jsonify, session
from model import User
from account import user_auth
import json

# root path 설정
account_bp = Blueprint('account_bp', __name__, url_prefix='/account')


@account_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':

        req_data = json.loads(request.get_data(), encoding='utf-8')

        user_id = req_data['user-id']
        user_pwd = req_data['password']

        res = user_auth.auth(user_id, user_pwd)

        return jsonify(res)

    return False


@account_bp.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':

        if 'user-id' in session:
            print('session clear.')
            session.pop('user-id')
        res = {'res-code': '203',
               'res-msg': '로그아웃 완료'}

        return jsonify(res)


@account_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        req_data = json.loads(request.get_data(), encoding='utf-8')

        # 데이터 검증 생략..
        # dup 에러도 생략...
        user_auth.register_user(req_data)

        return {
            'result': 'register success',
            'res-code': 202
        }


@account_bp.route('/userinfo', methods=['GET'])
def get_user_info_req():
    if request.method == 'GET':
        user_id = request.args['user-id']
        # 데이터 정검 생략..

        user_info = user_auth.get_user_info(user_id)
        session['user-id'] = user_id

        return jsonify(user_info)

    return False
