from flask import request, Blueprint, jsonify, session
import json
from df import process_dialogflow as df
from dataset import process_dataset
from db import process_db
from model.ErrorData import OracleErrorData

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

        print('[세션정보]', session.get('user-id', None))

        req_msg = req_data['msg']
        # proj-name, seesion-id, text, lang-code
        # dialogflow 호출
        # intent, res_msg_df = df.detect_intent_texts('fmpchat-udbn', '123456789', req_msg, 'ko-kr')
        # print(intent, res_msg_df)
        #
        # ### res code가 5이하이면, 수정해주어야됨
        # ### 10 -> 00010
        # if intent == '0000-chatIntent-custom':
        #     if len(res_msg_df) < 5:
        #         res_msg_df = '0'*(5-len(res_msg_df)) + res_msg_df
        #     error_code = 'ORA-' + res_msg_df
        #
        #     res_msg = oracle_errorzip[error_code].to_dict()
        #
        #     # 로그, 사용내역 적재
        #     process_db.insert_hist(req_data['user-id'], error_code)
        #     return jsonify(res_msg)
        # else :
        #     return jsonify(res_msg_df)

        ####################################################################
        intent, res_code = df.detect_intent_texts('chatbot-proj-295114', '123456789', req_msg, 'ko-kr')
        if intent == 'oracle_error':
            if len(res_code) < 5:
                res_code = '0'*(5-len(res_code)) + res_code
            error_code = 'ORA-' + res_code
            print('err code:', error_code)

            res_msg = oracle_errorzip[error_code].to_dict()

            # 로그, 사용내역 적재
            process_db.insert_hist(req_data['user-id'], error_code)
            return jsonify(res_msg)
        else:
            return jsonify(res_code)
        ####################################################################


'''
답변 등록
param : 
        user-id
        kind(oracle/proframe), 
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

            new_oracle_error_data = OracleErrorData(error_code=error_code,
                                                    situation=situation,
                                                    description=situation,
                                                    cause=cause,
                                                    solution=solution)

            user_id = req_data['user-id']
            res = process_db.insert_error_data(user_id, kind, new_oracle_error_data.to_dict())

            if res is False:
                return {'result': '이미 있는 데이터입니다.'}

            else:
                # refresh cash
                global oracle_errorzip
                oracle_errorzip = process_dataset.load_dataset('oracle_error')
                return {'result': 'success'}
        else:
            return {'result': '지원하지 않는 에러데이터 유형입니다.'}
    else :
        return {'result': '지원하지 않는 METHOD 입니다.'}

'''
사용내역 조회
param : user-id
return : hist-list(user-id, hist-list)
oracle, proframe별 구분 필요...
'''
# 사용내역 조회
@serving_bp.route('/userhist', methods=['GET'])
def get_user_hist():
    # param 없을경우 처리
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return '유저정보가 없습니다'

    # parameter 추출
    if request.method == 'GET':
        user_id = request.args['user-id']
        hist_list = process_db.select_hist_by_id(user_id)

        hist_list_detail = []
        for hist_data in hist_list:
            hist_detail = oracle_errorzip[hist_data['error-code']].to_dict()
            hist_detail['timestamp'] = hist_data['timestamp']
            hist_list_detail.append(hist_detail)

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