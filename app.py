from flask import Flask, request, jsonify, render_template
import json 


app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/api/v1/resources/books/all')
def all_books():
    return jsonify(books)

@app.route('/api/v1/resources/books')
def book_id():
    if id in request.args:
        id = int(request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
        
    for i in books:
        if i['id'] == id:
            return i['title']
                



app.run(host="172.27.183.209")