from flask import Flask 
from flask import request
from pyvi import ViTokenizer, ViPosTagger
app = Flask(__name__)


@app.route ('/',  methods=['POST']) 
def hello () :
	data = request.form['text']
	data = ViTokenizer.tokenize(data)
	return data

if __name__=="__main__":
	app.run()
	