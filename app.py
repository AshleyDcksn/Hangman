from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new_game')
def start_new_game():
    return render_template('new_game.html')

@app.route('/guess_letter/<string:letter>')
def guess_letter():
    return 'letter guess'

@app.route('/solve/<string:word>')
def solve():
    return 'solve'