#Project 4
#Maria Costello
#Prof. Arias
#April-2-2018


from graphics import *
from button import Button
import math

def createCalculatorGui():
  
    win = GraphWin("calculator", 550, 400)
    win.setCoords(0, .5, 9, 6.75)
    win.setBackground("orange")
    #scientific buttons
    bSpecs = [(.5,1,'ln'), (1.5,1,'10^x'), (2.5,1,"( )"),(3.5,1,'0'), (4.5,1,'.'),
          (.5,2,'tan^-1'), (1.5,2,'tan'), (2.5,2,'1'), (3.5,2,'2'), (4.5,2,'3'), (5.5,2,'+'), (6.5,2,'-'),
          (.5,3,'cos^-1'), (1.5,3,'cos'), (2.5,3,'4'), (3.5,3,'5'), (4.5,3,'6'), (5.5,3,'*'), (6.5,3,'/'),
          (.5,4,'sin^-1'), (1.5,4,'sin'), (2.5,4,'7'), (3.5,4,'8'), (4.5,4,'9'), (5.5,4,'<-'),(6.5,4,'C'),
          (.5,5,'log'), (1.5,5,'x^y'), (2.5,5,'MC'),(3.5,5,'M+'),(4.5,5,'M-'),(5.5,5,'MR'),(6.5,5,'MS')]
    
    buttons = createButtons(bSpecs, win)
    display = createDisplay(win)
    runDisp = runningDisplay(win)
    return buttons, display, win, runDisp

def createButtons(bSpecs, win):
    buttons = []
    for cx, cy, label in bSpecs:
        buttons.append(Button(win, Point(cx, cy), .75, .75, label))
    buttons.append(Button(win, Point(6,1), 1.50, .75, "="))
    for b in buttons:
        b.activate()
    return buttons

def createDisplay(win):
    bg = Rectangle(Point(.4, 5.75), Point(4, 6.5))
    bg.setFill('pink')
    bg.draw(win)
    text = Text(Point(1.75, 6.10), "")
    text.draw(win)
    text.setFace("courier")
    text.setStyle("bold")
    text.setSize(14)
    return text
def runningDisplay(win):
    rd = Rectangle(Point(4.5, 5.75), Point(7.5, 6.5))
    rd.setFill('pink')
    rd.draw(win)
    text = Text(Point(5.75,6.10), "")
    text.draw(win)
    text.setFace("courier")
    text.setStyle("bold")
    text.setSize(14)
    return text


def getButtonPressed(buttons, calc):
    while True:
        p = calc.getMouse()
        for b in buttons:
            if b.clicked(p):
                return b.getLabel()

def processButton(key, display, runDisp, memory):
    text = display.getText()
    memory = 0
    base = math.e
    if key == "<-":
        display.setText(text[:-1])
    
    elif key == "C":
        display.setText("")
        key = ""
        text = ""
    #memory keys
    elif key == "MC":
        memory = 0
    elif key == "M+":
        memory == memory + text
    elif key == "M-":
        memory == memory - text
    elif key == "MR":
        display.setText(result)
    elif key == "MS":
        memory = display.setText(memory)
    #science keys
    elif key == "log":
        display.setText(math.log10(int(text)))
    elif key == "x^y":
        display.setText(int(text)**int(text))
    elif key == "sin^-1":
        display.setText(math.asin(int(text)))
        try:
                result = (math.asin(int(text)))
        except:
                print("Cannot to divide by 0")
                result = 0
    elif key == "sin":
        display.setText(math.sin(int(text)))
    elif key == "cos^-1":
        display.setText(math.acos(int(text)))
        try:
                result = (math.acos(int(text)))
        except:
                print("Cannot to divide by 0")
                result = 0
    elif key == "cos":
        display.setText(math.cos(int(text)))
    elif key == "tan^-1":
        display.setText(math.atan(int(text)))
        try:
                result = (math.atan(int(text)))
        except:
                print("Cannot to divide by 0")
                result = 0
    elif key == "tan":
        display.setText(math.tan(int(text)))
    elif key == "ln":
        display.setText(math.log(int(text)))
    elif key == "10^x":
        display.setText(10 ** int(text))
    elif key == "( )":
        text = [(text)]
    elif key == "=":
        try:
            result = eval(text)
        except:
            result = "Error!!!"
        display.setText(result)
    else:
        display.setText(text + key)
    #fixed clear on second display    
    runDisp.setText(str(text) + str(key))
def main():
    buttons, display, calc, runDisp = createCalculatorGui()
    memory = 0
    while True:
        key = getButtonPressed(buttons, calc)
        print(key)
        processButton(key, display, runDisp, memory)


main()
