from pymongo import MongoClient, errors
from datetime import datetime
import sys

conn = MongoClient(host='20.41.82.195',
                       port=9017,
                       username='user1',
                       password='1q2w3e4r!')

database_name = 'fmp'
db = conn.get_database(database_name)


def insert_dataset(kind, dataset):
    if kind == 'oracle_error':
        collection = db.oracle_errorzip
        for data in dataset:
            insert_data = {
                'error_code': data[0],
                'situation': data[1],
                'description': data[2],
                'cause': data[3],
                'solution': data[4]
            }
            collection.insert_one(insert_data)

    # 추가필요..
    return True


def insert_error_data(kind, error_data):
    if kind == 'oracle_error':
        collection = db.oracle_errorzip
        # insert_data = {
        #     'error_code': error_data['error_code'],
        #     'situation': error_data['situation'],
        #     'description': error_data['description'],
        #     'cause': error_data['cause'],
        #     'solution': error_data['solution']
        # }
        print(error_data)
        collection.insert_one(error_data)

    return True


def insert_hist(user_id, error_code):
    collection = db.hist
    data = {'user-id': user_id, 'error-code': error_code, 'timestamp': datetime.utcnow()}
    try:
        collection.insert_one(data)
    except errors.DuplicateKeyError as dup_error:
        print(dup_error)
        return False
    except errors.WriteError as write_error:
        print(write_error)
        return False

    return True


def select_hist_by_id(user_id):
    collection = db.hist
    doc = list(collection.find({'user-id':user_id}, {'_id': False}))

    hist_list = []
    for hist in doc:
        hist_list.append(hist['error-code'])

    return hist_list
    # return {'user-id': user_id, 'hist-list': hist_list}


def load_dataset(kind):
    if kind == 'oracle_error':
        collection = db.oracle_errorzip
        doc = list(collection.find())
        return doc

    return None
    # return {'user-id': user_id, 'hist-list': hist_list}
