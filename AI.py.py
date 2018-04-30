#Maria Costello
#Lab8
#Prof. Arias
#April-10-2018


import random

emotionMatrix = [
    [4, 0, 0, 2],
    [2, 0, 0, 2], 
    [2, 3, 5, 2],
    [2, 3, 3, 2],
    [2, 3, 5, 2],
    [4, 3, 5, 2]
]

feelingslist = ["angry", "disgusted", "happy", "sad", "surprised", "fearful"]
actionslist = ["reward", "punish", "threaten", "joke"]
reactionlist = ["Grrr! That made me angry!", "Umm, eww! that is disgusting", "HA! you are awesome! That made me so happy", "Boohoo, you are going to make me cry like a baby", "Wait, what?! Very Surprising",  "Now I'm scared"]

def introduction():
    print("Hello. My name is Arty and I am an AI.")
    emotion = random.choice(feelingslist)
    indexfeeling = feelingslist.index(emotion)
    print("Today I am feeling kind of: " + emotion)
    return indexfeeling # JA
    

def getInteraction():
    userAction = input("What do you want to do to Al? (Type either reward, punish, joke or threaten): ")
    try:
        userAction = actionslist.index(userAction)
    except:
        userAction = 4
    return userAction

def lookupEmotion(currEmotion, userAction):
    newemotion = emotionMatrix[currEmotion][userAction]
    return newemotion
def main():
    goonforever = True
    currEmotion = introduction()
    while goonforever == True:
        userAction = getInteraction()
        if userAction == 4:
            print("Invalid Action")
            print('\n')
            continue
        else:
            currEmotion = lookupEmotion(currEmotion, userAction)
            print(reactionlist[currEmotion])
            print('\n')
    return


main()
