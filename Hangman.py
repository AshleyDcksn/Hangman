__author__ = 'Ashley'
class NewHangmanGame:
  #  word=""
  #  word_length=0
  #  number_of_tries = -1

    def __init__(self, _id, _word, _word_length):
        self.id = _id
        self.word = _word
        self.word_length = _word_length
        self.number_of_tries = 6
        self.index_list = []