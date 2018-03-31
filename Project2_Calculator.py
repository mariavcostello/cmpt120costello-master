#Maria Costello
#Project 2 Calculator
#Intro to Programming
#March 11, 2018

from graphics import *
from button import *
from math import *
buttons = []


#buttons are formed 
def create_button(win, x1, y1, x2, y2, label, color = 'pink'):
    button = Rectangle(Point(x1,y1), Point(x2, y2))
    button.setFill(color)
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.setSize(10)
    text.draw(win)
    return button, label


def check(button, label, x, y):
    x1 = button.p1.getX()
    y1 = button.p1.getY()
    x2 = button.p2.getX()
    y2 = button.p2.getY()
    if x > x1 and x < x2 and y > y1 and y < y2:
        return label
    return False
#calculation is preformed
def calculation(answer, entry, operation):
    if answer == None:
        answer = entry
        entry = 0
    else:
        if operation == '+':
            answer = addition(answer, entry)
        elif operation == '-':
            answer = subtraction(answer, entry)
        elif operation == '*':
            answer = multiplication(answer, entry)
        elif operation == '/':
            answer = division(answer, entry)
        elif operation == '+/-':
            answer = change_sign(answer)
        elif operation == 'x2':
            answer = square(answer)
        elif operation == '%':
            answer = percent(answer)
        elif operation == '√':
            answer = square_root(answer)
        elif operation == '1/x':
            answer = over_x(answer)
        entry = 0
    return answer, entry

#calculator is formed_buttons
def main():
    win = GraphWin("Calc", 300, 660)

    displayScreen = Rectangle (Point(10,10), Point(275,75))
    displayScreen.setFill('gray')
    displayScreen.draw(win)

    buttons.append(create_button (win, 8, 115, 73, 187, "7", 'lightblue'))
    buttons.append(create_button (win, 8, 192, 73, 264, "4", 'lightblue'))
    buttons.append(create_button (win, 8, 269, 73, 341, "1", 'lightblue'))
    buttons.append(create_button (win, 8, 346, 73, 418, "+/-", 'gray'))
    buttons.append(create_button (win, 8, 423, 73, 495, "X2", 'gray'))
    buttons.append(create_button (win, 8, 500, 73, 572, "MC", 'lightgreen'))
    buttons.append(create_button (win, 8, 577, 73, 649, "M+", 'lightgreen'))
    buttons.append(create_button (win, 81, 115, 146, 187, "8", 'lightblue'))
    buttons.append(create_button (win, 81, 192, 146, 264, "5", 'lightblue'))
    buttons.append(create_button (win, 81, 269, 146, 341, "2", 'lightblue'))
    buttons.append(create_button (win, 81, 346, 146, 418, "0", 'lightblue'))
    buttons.append(create_button (win, 81, 423, 146, 495, "√", 'gray'))
    buttons.append(create_button (win, 81, 500, 146, 572, "M-", 'lightgreen'))
    buttons.append(create_button (win, 81, 577, 146, 649, "MR", 'lightgreen'))
    buttons.append(create_button (win, 154, 115, 219, 187, "9", 'lightblue'))
    buttons.append(create_button (win, 154, 192, 219, 264, "6", 'lightblue'))
    buttons.append(create_button (win, 154, 269, 219, 341, "3", 'lightblue'))
    buttons.append(create_button (win, 154, 346, 219, 418, ".", 'orange'))
    buttons.append(create_button (win, 154, 423, 219, 495, "1/x", 'gray'))
    buttons.append(create_button (win, 154, 500, 219, 572, "C", 'gray'))
    buttons.append(create_button (win, 154, 577, 219, 649, "MS", 'lightgreen'))
    buttons.append(create_button (win, 227, 115, 292, 187, "/", 'orange'))
    buttons.append(create_button (win, 227, 192, 292, 264, "*", 'orange'))
    buttons.append(create_button (win, 227, 269, 292, 341, "+", 'orange'))
    buttons.append(create_button (win, 227, 346, 292, 418, "-", 'orange'))
    buttons.append(create_button (win, 227, 423, 292, 495, "%", 'orange'))
    buttons.append(create_button (win, 227, 500, 292, 572, "=", 'orange'))
    buttons.append(create_button (win, 227, 577, 292, 649, "", 'white'))

    displayString = ''
    displayTextElement = Text(Point(250,120), "")
    displayTextElement.draw(win)
    answer = None
    entry = 0
    operation = None
    clearNextNumber = False
    memory = 0
    entryString = ''

    while 1 == 1:
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        for b in buttons:
            button, label = b
            key = check(button, label, x, y)
            if key:
                if key == '=':
                    clearNextNumber = True
                    if answer == None:
                        answer = entry
                        displayString = str(answer)
                        entry = 0
                        entryString = ''
                    else:
                        answer, entry = calculation(answer, entry, operation)
                        operation = None
                        displayString = '%20.3f' % (answer) 

                elif key in ['+', '-', '/', '*', '%']:
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = displayString + key
                    clearNextNumber = False
                    
                elif key == '+/-':
                    answer, entry = calculation(answer, entry, operation)                        
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'x2':
                    answer, entry = calculation(answer, entry, operation)
                    operation = key
                    displayString = str(answer) + str('^2')
                    clearNextNumber = True

                elif key  == '√':
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = key + str(answer)
                    clearNextNumber = True

                elif key == '1/x':
                    x = entry
                    answer, entry = calculation(answer, entry, operation)
                    entryString = ''
                    operation = key
                    displayString = str(answer)
                    clearNextNumber = True

                elif key == 'C':
                    displayString = ''
                    answer = None
                    entry = 0
                    entryString = ''
                    operation = None

                elif key == 'M+':
                    memory = addition(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MR':
                    displayString = float(memory)
                    
                elif key == 'M-':
                    memory = subtraction(float(memory), entry or answer)
                    displayString = float(memory)

                elif key == 'MC':
                    memory = 0

                elif key == 'MS':
                    temp = memory
                    memory = entry
                    entry = temp
                    displayString = float(memory)

                else:
                    if clearNextNumber:
                        displayString = ''
                        clearNextNumber = False
                        answer = None
                        entry = 0
                        entryString = ''
                        operation = None
                    entryString = entryString + key
                    entry = float(entryString) 
                    displayString = displayString + key

                displayTextElement.undraw()
                displayTextElement = Text(Point(100, 25), displayString)
                displayTextElement.setFace('courier')
                displayTextElement.setSize(14)
                displayTextElement.draw(win)
####################Functions
def addition(num1, num2):
    result = num1 + num2
    return float (result)

def subtraction(num1, num2):
    result = num1 - num2
    return float (result)

def multiplication(num1, num2):
    result = num1 * num2
    return float (result)

def division(num1, num2):
    result = num1 / num2
    return float (result)

def change_sign(num1):
    result = (num1 * -1)
    return float (result)

def square(num1):
    result = num1 * num1
    return float (result)

def square_root (num1):
    result = sqrt(num1)
    return float (result)

def percent (num1):
    result = num1 / 100
    return float (result)

def over_x(num1):
    x = num1
    result = 1 / x
    return float (result)
#Functions####################


main()
