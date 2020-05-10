from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('assignment3.html')

@app.route('/', methods=['POST'])
def search_form():
	search_word = request.form['Search_Item']
	dropdown = request.form.get('search_type')

	if(dropdown == 'Author'):
		y = requests.get("http://100.24.21.95:2000/search_author/{}".format(search_word)).json()
	else:
		y = requests.get("http://100.24.21.95:2000/search_book/{}".format(search_word)).json()
	
	flag = True
	if(len(y) == 0):
		flag = False
	return render_template('assignment3.html', word=search_word, data=y, abflag=flag)

@app.route('/submitnote', methods=['POST'])
def submit_note():

	note = request.form['notes']
	search_word = request.form['search_word']

	requests.get("http://100.24.21.95:2000/submitnotes/{}/{}".format(search_word,note))

	return render_template('assignment3.html', submitresponse="Note submitted", notesubmittedflag=True, word=search_word)

@app.route('/retrievenotes', methods=['POST'])
def retrieve_notes():

	search_word = request.form['search_word']

	y = requests.get("http://100.24.21.95:2000/searchnotes/{}".format(search_word)).json()
	
	notesfoundflag = True
	msg = "notes found"
	if(len(y) == 0):
		notesfoundflag = False
		msg = "no notes found"

	return render_template('assignment3.html', submitresponse=msg, notes=y, notesfoundflag=notesfoundflag, word=search_word)

if __name__ == '__main__':
	app.run(debug=True, port = 1999)
