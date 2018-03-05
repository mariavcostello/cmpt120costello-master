# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Maria C
# Created: 2018-03-2
animal= "frog"
def main ():
    while True :
        print ("Thinking of an animal.")
        guess = input ("What is your guess?")
        if guess.lower () == animal.lower :
            print ("Congratulations! That is correct")
            break
        elif guess == "quit":
            break
        else:
            print ("Sorry, try again")
        
main ()
    
