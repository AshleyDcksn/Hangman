from flask import Flask, session
from flask import render_template
from flask import request
from flask.ext.mysql import MySQL
import os
import random
import configureDB
import Hangman

app = Flask(__name__)
app.secret_key = os.urandom(24)
mysql = MySQL()
configureDB.configure(app)
mysql.init_app(app)
hmGame = None


@app.route('/')
def hello_world():
    return render_template('hang_man.html')

@app.route('/new_game')
def start_new_game():
    word_index = random.randint(1,14)
    conn = mysql.connect()
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT word, word_length FROM dev.hang_man_tbl where idhang_man=(%s)",(word_index))
    row = list(cursor.fetchone())
    global hmGame
    hmGame = Hangman.NewHangmanGame(word_index, row[0],row[1])
    conn.close()
    return render_template('new_game.html', hm=hmGame)

#TODO Add method for user to submit a char
@app.route('/add_char', methods=['POST'])
def add_char():
    letter = request.form['letter']
    global hmGame
    hmWord = hmGame.word
    letter_indexes = [pos for pos, char in enumerate(hmWord) if char == letter]
    if len(letter_indexes) == 0:
        hmGame.number_of_tries -= 1
    else:
        hmGame.index_list.extend(letter_indexes)
    return render_template('game_1.html', hm=hmGame)



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
