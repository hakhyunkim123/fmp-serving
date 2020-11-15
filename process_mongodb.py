# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests

import _process_mongodb


def saveForm():
    print("come saveForm?")
    if request.method == "POST":
        swname = request.form['name']
        userId = request.form['email']
        phoneNum = request.form['phone']
        content = request.form['message']
        datas = {'swname': swname, 'userid': userId, 'phonemum': phoneNum, 'content': content}
        print(datas)
        res = requests.post(INPUT_URL, data=datas)
        if res.text == "SUCCESS":
            print("SAVE SUCCESS")
    return render_template('input_form.html')


def mongoSave():
    print("come saveMongo?")
    client = MongoClient('mongodb://localhost:27017/')
    db = client.newDatabase
    collection = _process_mongodb.mongoTest
    name = request.form['name']
    content = request.form['content']
    mdict = {'name': name, 'content': content}
    print(mdict)
    collection.insert_one(mdict)
    return redirect(url_for('mongoTest'))


def mongoDelete():
    print("come deleteMongo?")
    client = MongoClient('mongodb://localhost:27017/')
    db = client.newDatabase
    collection = _process_mongodb.mongoTest
    idNum = request.form['idNum']
    collection.delete_one({'_id': ObjectId(idNum)})
    return redirect(url_for('mongoTest'))


