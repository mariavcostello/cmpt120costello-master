#Maria Costello
#Intro to Programming 
#Prof. Arias
#Lab Assignment 10

from simstats import SimStats

from tennismatch import TennisGame



def printIntro():
    print ("This is a simulation of a tennis game. A match includes three sets")
    print ('and you must win at least 6 games. If a set is 6-5, then the first')
    print ('player needs one more set to win while the second player would need')
    print ('two. If the games are tied at 6 in a set, a tie breaker is played.')
    print ('Games are scored  15, 30, 40. If a player has 40, the next point won')
    print ('will win the set. The player serving will serve the whole game.If the game')
    print ('ties at 40(deuce), the player who wins two points in a row wins the game.\n')

def getInputs():

    probA = float(input("Enter the probability of A: "))

    probB = float(input("Enter the probability of B: "))

    n = int(input("Number of games to simulate: "))

    return probA, probB, n  

def main():

    printIntro()

    probA, probB, n = getInputs()

    stats = SimStats()

    for i in range(n):

        theGame = TennisGame(probA, probB)

        theGame.play()

        stats.update(theGame)

    stats.printReport()



main()
