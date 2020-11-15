# from flask import Flask, render_template, redirect, request, url_for
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# import os, requests
# import json
# app = Flask(__name__)
#
# # 질문 메세지 처리
# @app.route('/req/question', methods=['POST'])
# def request_question():
#     if request.method == 'POST':
#         # body데이터 추출
#         req_msg = request.get_json()
#
#     # else -> 지원하지 않는..
#     # dialogflow 호출
#     # entity, intent 추출
#     # res msg gen
#     # 데이터/로그 적재
#     # return
#
# # 사용내역 조회
# @app.route('/userhist', methods=['GET'])
# def get_user_hist():
#     #param 없을경우 처리
#     parameter_dict = request.args.to_dict()
#     if len(parameter_dict) == 0:
#         return '유저정보가 없습니다'
#
#     # parameter 추출
#     if request.method == 'GET':
#         user_id = request.args['user-id']
#         # select history data
#     # gen history list
#     # 로그 적재
#     # return
#
# # 답변등록
# @app.route('/add/answer', methods=['POST'])
# def add_answer():
#     # body 데이터 처리
#     # intent, entity, respose 추출
#     # gen data
#     # call dialogflow api
#     # if OK -> return OK
#
#
# if __name__ == '__main__':
#     # 에러코드집 캐싱
#     app.run(host='0.0.0.0', port='5000')