from db import process_db
from model.User import User


def auth(user_id, user_pwd):
    user_info = process_db.select_user(user_id)

    res = dict()

    if user_info is None:
        res['res_code'] = 301
        res['res_msg'] = '존재하지 않는 아이디입니다.'
        return res

    elif user_info['pwd'] != user_pwd:
        res['res_code'] = 302
        res['res_msg'] = '비밀번호가 틀렸습니다.'
        return res

    else:
        res['res_code'] = 201
        res['user-info'] = user_info
        res['res_msg'] = '로그인 성공.'
        return res


def register_user(user_data):
    sql_result = process_db.insert_user(user_data)
    res = dict()

    if sql_result is True:
        res['res-code'] = 202
        res['res-msg'] = '회원가입 성공'
    else:
        res['res-code'] = 303
        res['res-msg'] = '회원가입 실패'

    return res


def get_user_info(user_id):
    user_info = process_db.select_user(user_id)

    return user_info
