#Maria Costello
#Intro to Programming 
#Prof. Arias
#Lab Assignment 10

from tennisplayer import Player

from math import *


class TennisGame:

    def __init__(self, probA, probB):

        self.playerA = Player(probA)

        self.playerB = Player(probB)

        self.server = self.playerA

        self.aWon = 0

        self.bWon = 0

    def play(self):

        winner = 0

        while winner<3:

            self.game()

            winner = winner +1

            self.aWon,self.bWon=0,0     

    def game(self):

        while not self.isOver():

            if self.server.winsServe():

                self.server.incScore()

            else:

                self.changeServer()

        if self.playerA.getScore() > self.playerB.getScore():

            self.aWon = self.aWon + 1

        else:

            self.bWon = self.bWon + 1

    def getScores(self):

        return self.playerA.getScore(), self.playerB.getScore()

    def isOver(self):

        return (self.playerA.getScore() >=40  or self.playerB.getScore() >=40)

            and abs(self.playerA.getScore()-self.playerB.getScore())>=30

    def changeServer(self):

        if self.server == self.playerA:

            self.server = self.playerB

        else:

            self.server = self.playerA
