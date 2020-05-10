import flask
from flask import jsonify
import requests
import json

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/search_book/<book>', methods=['GET'])
def search_book(book):

    x = requests.get("http://100.24.21.95:2001/log/{}".format(book)).json()
    y = requests.get("http://100.24.21.95:2002/catalog_book/{}".format(book)).json()

    return jsonify(list(y))
    
@app.route('/search_author/<author>', methods=['GET'])
def search_author(author):

    x = requests.get("http://100.24.21.95:2001/log/{}".format(author)).json()
    y = requests.get("http://100.24.21.95:2002/catalog_author/{}".format(author)).json()
    
    return jsonify(list(y))

@app.route('/submitnotes/<word>/<note>', methods=['GET'])
def submit_notes(word,note):

    y = requests.get("http://100.24.21.95:2003/submitnotes/{}/{}".format(word,note)).json()

    return jsonify(list(y))

@app.route('/searchnotes/<word>', methods=['GET'])
def search_notes(word):

	y = requests.get("http://100.24.21.95:2003/searchnotes/{}".format(word)).json()
	
	return jsonify(list(y))

app.run(host='0.0.0.0',port=2000)