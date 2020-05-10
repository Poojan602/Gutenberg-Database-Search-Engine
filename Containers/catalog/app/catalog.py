import flask
from flask import jsonify
import json
import pymongo

app = flask.Flask(__name__)

app.config["DEBUG"] = True

client = pymongo.MongoClient("mongodb://Poojan:Poojan@100.24.21.95/Cloud_Assignment")

db = client.Cloud_Assignment

collection = db.Author_Book
collection2 = db.catalog

@app.route('/catalog_book/<book>', methods=['GET'])
def catalog_book(book):

    tobe_searched = { "Book": book }

    x1 = collection2.find(tobe_searched,{"_id":0, "Book": 1, "Author": 1 })

    if (x1.count() == 0):
        x = collection.find(tobe_searched,{ "_id": 0, "Book": 1, "Author": 1 })
        if(x.count() != 0):
            collection2.insert_many(x)

    x1 = collection2.find(tobe_searched,{"_id":0, "Book": 1, "Author": 1 })
    
    if(x1.count() == 0):
        return jsonify([])
    else:
        return jsonify(list(x1))

@app.route('/catalog_author/<author>', methods=['GET'])
def catalog_author(author):

    tobe_searched = { "Author": author }

    x1 = collection2.find(tobe_searched,{"_id":0, "Book": 1, "Author": 1 })

    if (x1.count() == 0):
        x = collection.find(tobe_searched,{ "_id": 0, "Book": 1, "Author": 1 })
        if(x.count() != 0):
            collection2.insert_many(x)

    x1 = collection2.find(tobe_searched,{"_id":0, "Book": 1, "Author": 1 })
    
    if(x1.count() == 0):
        return jsonify([])
    else:
        return jsonify(list(x1))

app.run(host='0.0.0.0',port=2002)