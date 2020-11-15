# from flask import render_template
# from pymongo import MongoClient
#
#
# def mongoTest():
#     print("come?")
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client.newDatabase
#     collection = db.mongoTest
#     results = collection.find()
#     client.close()
#     return render_template('mongo.html', data=results)