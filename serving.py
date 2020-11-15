from flask import request, Blueprint, jsonify
import json
from df import process_dialogflow as df
from dataset import process_dataset
from db import process_db

# root path 설정
serving_bp = Blueprint('serving_bp', __name__, url_prefix='/serving')

# oracle_errorzip = dict()
oracle_errorzip = process_dataset.load_dataset('oracle_error')


# 질문 메세지 처리
# param : user-id, msg
# return : res_msg(json)
@serving_bp.route('/req/question', methods=['POST'])
def request_question():
    if request.method == 'POST':
        # body데이터 추출
        req_data = json.loads(request.get_data(), encoding='utf-8')

        req_msg = req_data['msg']
        # proj-name, seesion-id, text, lang-code
        # dialogflow 호출
        intent, res_code = df.detect_intent_texts('chatbot-proj-295114', '123456789', req_msg, 'ko-kr')
        print(intent, res_code)

        if intent == 'oracle_error':
            if len(res_code) == 4:
                res_code = '0' + res_code
            error_code = 'ORA-' + res_code

            res_msg = oracle_errorzip[error_code].to_dict()
            
            # 로그, 사용내역 적재
            process_db.insert_hist(req_data['user-id'], error_code)
            return jsonify(res_msg)
        else:
            return '몰라..'


'''
답변 등록
param : kind(oracle/proframe), 
        error_code(에러코드), 
        situation(현상), 
        cause(원인), 
        solution(조치)
return : 200
'''
@serving_bp.route('/add/answer', methods=['POST'])
def add_answer():
    if request.method == 'POST':
        # body데이터 추출
        req_data = json.loads(request.get_data(), encoding='utf-8')

        kind = req_data['kind']
        if kind == 'oracle_error':
            error_code = req_data['error_code']
            situation = req_data['situation']
            cause = req_data['cause']
            solution = req_data['solution']

            error_code = 'ORA-' + '0' * (9 - len(error_code)) + error_code[4:len(error_code)]

            new_oracle_error_data = process_dataset.OracleErrorData(error_code=error_code,
                                                    situation=situation,
                                                    description=situation,
                                                    cause=cause,
                                                    solution=solution)

            process_db.insert_error_data(kind, new_oracle_error_data.to_dict())

            # refresh cash!!!!

    return {'res' : 'suc'}

'''
답변 등록
param : user-id
return : hist-list(user-id, hist-list)
oracle, proframe별 구분 필요...
'''
# 사용내역 조회
@serving_bp.route('/userhist', methods=['GET'])
def get_user_hist():
    #param 없을경우 처리
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return '유저정보가 없습니다'

    # parameter 추출
    if request.method == 'GET':
        user_id = request.args['user-id']
        hist_list = process_db.select_hist_by_id(user_id)

        hist_list_detail = []
        for error_code in hist_list:
            hist_list_detail.append(oracle_errorzip[error_code].to_dict())

        return jsonify({'user-id': user_id, 'hist-list': hist_list_detail})
        # select history data
    # gen history list
    # 로그 적재
    return None


'''
데이터셋 DB저장
param : kind
return : OK
oracle, proframe별 구분 필요...
'''
@serving_bp.route('/save/dataset', methods=['GET'])
def save_dataset():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return '유형정보 없음'

    if request.method == 'GET':
        kind = request.args['kind']
        result = process_dataset.save_dataset(kind)

        return {'res': result}

    return None