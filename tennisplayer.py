#Maria Costello
#Intro to Programming 
#Prof. Arias
#Lab Assignment 10

from random import *

class Player:

    def __init__(self, prob):

        self.prob = prob

        self.score = 0

    def winsServe(self):

        return random() <= self.prob

    def incScore(self):

        # Add a point to this player's score

        self.score = self.score + 15

    def getScore(self):

        #Player's current score

        return self.score
