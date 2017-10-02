__author__ = 'Ashley'
class Hangman:
    word=""
    word_length=0
    number_of_tries = -1

    def function(self, word, word_length):
        self.word = word
        self.word_length = word_length
        self.number_of_tries = 7