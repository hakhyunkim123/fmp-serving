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
                'register': 'admin',
                'error_code': data[0],
                'situation': data[1],
                'description': data[2],
                'cause': data[3],
                'solution': data[4],
                'timestamp': datetime.utcnow()
            }

            try:
                collection.insert_one(insert_data)
            except errors.DuplicateKeyError as dup_error:
                print(insert_data['error_code'])
                # return False

            # collection.insert_one(insert_data)

    # 추가필요..
    return True


def insert_error_data(user_id, kind, error_data):
    if kind == 'oracle_error':
        collection = db.oracle_errorzip

        # 해당 에러코드에 대한 데이터가 이미 있으면, False
        error_data_db = list(collection.find({'error_code': error_data['error_code']}, {'_id': False}))
        if len(error_data_db) > 0:
            return False

        error_data['register'] = user_id
        error_data['timestamp'] = datetime.utcnow()
        collection.insert_one(error_data)

    return True


def insert_hist(user_id, error_code):
    collection = db.hist
    data = {'user-id': user_id, 'error-code': error_code}

    hist = collection.find_one(data)
    if hist is not None:
        print('update:', hist['_id'])
        collection.delete_one({'_id': hist['_id']})

    data['timestamp'] = datetime.utcnow()
    collection.insert_one(data)

    return True

    # try:
    #     collection.insert_one(data_with_date)
    # except errors.DuplicateKeyError as dup_error:
    #     update_data = {'$set': data_with_date}
    #     print('update!')
    #     collection.update_one(data, update_data)
    #     return True
    # except errors.WriteError as write_error:
    #     print(write_error)
    #     return False


def select_hist_by_id(user_id):
    collection = db.hist
    hist_list = list(collection.find({'user-id': user_id}, {'_id': False}).sort('timestamp', -1))

    # hist_list = []
    # for hist in doc:
    #     hist_list.append(hist['error-code'])

    return hist_list
    # return {'user-id': user_id, 'hist-list': hist_list}


def load_dataset(kind):
    if kind == 'oracle_error':
        collection = db.oracle_errorzip
        doc = list(collection.find())
        return doc

    return None
    # return {'user-id': user_id, 'hist-list': hist_list}


def select_user(user_id):
    collection = db.user
    user_dict = collection.find_one({'employ_num': user_id}, {'_id': False})

    return user_dict


def insert_user(user_data):
    collection = db.user
    collection.insert_one(user_data)

    return True
