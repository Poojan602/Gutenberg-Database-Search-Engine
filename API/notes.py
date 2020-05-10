import flask
from flask import jsonify
import json
import pymongo
import os.path
from os import path

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/submitnotes/<word>/<note>', methods=['GET'])
def submit_notes(word,note):

    if(path.exists("/Users/patelpoojan/Desktop/Acloud_assignment3/notes.txt")):

        with open('notes.txt') as json_file:
            data = json.load(json_file) 

        flag = False

        for i in data:
            if(i['Word'] == word):
                y = {}
                y['Note'] = note
                i['Notes'].append(y)
                flag = True
                break

        if(flag == False):
            y = {}
            y['Word'] = word
            notelist = []
            dnote = {}
            dnote['Note'] = note
            notelist.append(dnote)
            y['Notes'] = notelist
            data.append(y)

        with open('notes.txt','w') as f: 
            json.dump(data, f, indent=4)

    else:
        l = []
        y = {}
        y['Word'] = word
        notelist = []
        dnote = {}
        dnote['Note'] = note
        notelist.append(dnote)
        y['Notes'] = notelist
        l.append(y)
            
        with open('notes.txt','x') as json_file:
            json.dump(l,json_file, indent=4)

    return "Note Submitted"

@app.route('/searchnotes/<word>', methods=['GET'])
def search_notes(word):

    lst = []

    if(path.exists("/Users/patelpoojan/Desktop/Acloud_assignment3/notes.txt")):
        
        with open('notes.txt') as f:
            data = json.load(f)

        for i in data:
            if(i['Word']==word):
                for ns in i['Notes']:
                    lst.append(ns)

        if(len(lst)==0):
            return jsonify([])
      
        return jsonify(lst)

    else:
        return jsonify([])

app.run(port=2003)