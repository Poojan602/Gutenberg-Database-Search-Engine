import flask
from flask import jsonify
import json
import datetime
import os.path
from os import path

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/log/<word>', methods=['GET'])
def log(word):

    if(path.exists("/Users/patelpoojan/Desktop/Acloud_assignment3/log.txt")):

        with open('log.txt') as json_file:
            data = json.load(json_file)

        flag = False

        for i in data:
            if(i['Word']==word):
                i['Frequency'] += 1
                dtime = {}
                current_time = datetime.datetime.now()
                dtime['Time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
                i['Times'].append(dtime)
                flag = True
                break
        
        if(flag == False):
            y = {}
            y['Word'] = word
            y['Frequency'] = 1
            timelist = []
            dtime = {}
            current_time = datetime.datetime.now()
            dtime['Time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
            timelist.append(dtime)
            y['Times'] = timelist
            data.append(y) 

        with open('log.txt','w') as f: 
            json.dump(data, f, indent=4) 

    else:
        l = []
        y = {}
        y['Word'] = word
        y['Frequency'] = 1
        timelist = []
        dtime = {}
        current_time = datetime.datetime.now()
        dtime['Time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")
        timelist.append(dtime)
        y['Times'] = timelist
        l.append(y) 
        
        with open('log.txt','x') as json_file:
            json.dump(l,json_file, indent=4)

    return jsonify([])

app.run(port=2001)