from flask import Flask
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
NUMBER_OF_ROWS = 14

@app.route('/')
def hello_world():
    return render_template('hang_man.html')

@app.route('/new_game')
def start_new_game():
    word_selector_id = random.randint(1,NUMBER_OF_ROWS)
    conn = mysql.connect()
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT word, word_length FROM dev.hang_man_tbl where idhang_man=(%s)",(word_selector_id))
    row = list(cursor.fetchone())
    global hmGame
    hmGame = Hangman.NewHangmanGame(word_selector_id, row[0],row[1])
    conn.close()
    return render_template('new_game.html', hm=hmGame)

@app.route('/add_char', methods=['POST'])
def add_char():
    letter = request.form['letter']
    global hmGame
    hmWord = hmGame.word
    hmGame.alphaDict[letter] = 0
    letter_indexes_found = [pos for pos, char in enumerate(hmWord) if char == letter]
    if len(letter_indexes_found) == 0:
        hmGame.number_of_tries -= 1
        if hmGame.number_of_tries == 0:
            return render_template('loser.html',hm=hmGame)
        else:
            return render_template('game_1.html', hm=hmGame)
    elif letter_indexes_found in hmGame.index_list: ##TODO: Case where same letter is entered twice!!
        return render_template('game1.html', hm=hmGame)
    elif len(hmGame.index_list) == hmGame.word_length:
        #user won the game!
        return render_template('winner.html', hm=hmGame)
    else:
        hmGame.index_list.extend(letter_indexes_found)
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
