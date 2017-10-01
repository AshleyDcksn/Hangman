from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hang_man.html')

@app.route('/new_game')
def start_new_game():
    return render_template('new_game.html')

#TODO Add method for user to submit a char
@app.route('/add_char', methods=['POST'])
def add_char():
    my_char = request.form['letter']
    return redirect(url_for('show_entries'))

#TODO Add method to return template based on char
@app.route('/show_game_1')
def show_entries():
    return render_template('game_1.html')

@app.route('/guess_letter/<string:letter>')
def guess_letter():
    return 'letter guess'

@app.route('/solve/<string:word>')
def solve():
    return 'solve'