from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new_game')
def start_new_game():
    return render_template('new_game.html')

#TODO Add method for user to submit a char
#@app.route('/add', methods=['POST'])
#def add_char():
#    my_char = request.form['char']
#    return redirect(url_for('show_entries'))
#TODO Add method to return template based on char
#@app.route('/')
#def show_entries():
#    entries = cur.fetchall()
#    return render_template('show_entries.html', entries=entries)

@app.route('/guess_letter/<string:letter>')
def guess_letter():
    return 'letter guess'

@app.route('/solve/<string:word>')
def solve():
    return 'solve'