from graphics import *
import math

win = GraphWin('Calc', 320, 500)

# Create text for the display area

displayTextElement = Text(Point(0, 50), "")

calcGrid = [
    [7, 8, 9, '+'],
    [4, 5, 6, '-'],
    [1, 2, 3, '*'],
    [0, 'C','=','/'],
    ['', '', '', '']
]
buttons = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]

def calcButton(x, y, value):
    button = Rectangle(Point(x,y),Point(x + 90,y + 90))
    button.setFill('purple')
    button.draw(win)
    text = Text(Point(x + 50, y + 50), value)
    text.draw(win)
    return button

def sum (n1, n2):
    return n1+n2
def sub (n1, n2):
    return n1-n2
def mul (n1, n2):
    return n1*n2
def div (n1, n2):
    return n1/n2

def operation():

    if operation == '+':
        result = sum(num1, num2)
    elif operation == '-' :
        result = sub(num1, num2)
    elif operation == '*' :
        result = mul(num1, num2)
    elif operation == '=' :
        result = answer
    elif operation == '/' :
        result = div(num1, num2)
    else:
        pass
    
def inside(clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY()and clicked.getY() < button.p2.getY():
                return True
    return False

def clickedButton(clicked):
    for i in range(5):
        for j in range(4):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(5):
        for j in range(4):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 60), "")
    displayTextElement.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        if row > 0:
            buttons[row][col].setFill('lightgreen')
            displayString = (displayString + str(calcGrid[row][col])).rjust(135);
            displayTextElement.undraw()
            displayTextElement = Text(Point(0, 60), displayString)
            displayTextElement.draw(win)
            print (calcGrid[row][col])
        for i in range(5):
            for j in range(4):
                if not(i == row and j == col):
                    buttons[i][j].setFill('purple')


main()



