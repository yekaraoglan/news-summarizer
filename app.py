import transformers
import json

from flask import (
	Flask,
	request
)

summarizer = transformers.pipeline('summarization', 'yekaraoglann/results')

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/predict', methods=['POST'])
def predict():
	args = request.json
	summary = summarizer(args['text'], min_length=5, max_length=100)
	return json.dumps({'summary': summary})
