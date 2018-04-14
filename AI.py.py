#Maria Costello
#Lab8
#Prof. Arias
#April-10-2018


import random


def introduction():
    print("Hello. My name is Arty and I am an AI.")
    emotion = random.choice(feelingslist)
    indexfeeling = feelingslist.index(emotion)
    print("Today I am feeling kind of: " + emotion)
    

# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction():
pass # TODO prompt user to choose an action
return 0 # return a corresponding integer
# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion
def lookupEmotion(currEmotion, userAction):
pass # TODO do the matrix lookup
return 0 # return an integer corresponding to an emotion


main()
