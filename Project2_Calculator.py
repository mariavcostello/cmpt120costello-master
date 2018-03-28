#Maria Costello
#Project 2 Calculator
#Intro to Programming
#March 11, 2018

from graphics import *
from button import *
from math import *
buttons = []



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


def main():
    win = GraphWin("Calc", 350, 527)

    displayScreen = Rectangle (Point(5,5), Point(250,55))
    displayScreen.setFill('gray')
    displayScreen.draw(win)

    buttons.append(create_button (win, 5.72, 81.51, 52.195, 133.705, "7", 'lightyellow'))
    buttons.append(create_button (win, 5.72, 137.28, 52.195, 188.76, "4", 'lightyellow'))
    buttons.append(create_button (win, 5.72, 191.835, 52.195, 243.815, "1", 'lightyellow'))
    buttons.append(create_button (win, 5.72, 247.39, 52.195, 298.87, "+/-", 'lightblue'))
    buttons.append(create_button (win, 5.72, 302.445, 52.195, 353.925, "x2", 'lightblue'))
    buttons.append(create_button (win, 5.72, 357.5, 52.195, 408.98, "MC", 'lightblue'))
    buttons.append(create_button (win, 5.72, 412.555, 52.195, 464.035, "MR", 'lightblue'))
    buttons.append(create_button (win, 57.915, 82.225, 104.39, 133.705, "8", 'lightyellow'))
    buttons.append(create_button (win, 57.915, 137.28, 104.39, 188.76, "5", 'lightyellow'))
    buttons.append(create_button (win, 57.915, 192.335, 104.39, 243.815, "2", 'lightyellow'))
    buttons.append(create_button (win, 57.915, 247.39, 104.39, 298.87, "0", 'lightyellow'))
    buttons.append(create_button (win, 57.915, 302.445, 104.39, 353.925, "√", 'lightblue'))
    buttons.append(create_button (win, 57.915, 357.5, 104.39, 408.98, "M-", 'lightblue'))
    buttons.append(create_button (win, 57.915, 412.555, 104.39, 464.035, "MS", 'lightblue'))
    buttons.append(create_button (win, 110.11, 82.225, 156.585, 133.705, "9", 'lightyellow'))
    buttons.append(create_button (win, 110.11, 137.28, 156.585, 189.19, "6", 'lightyellow'))
    buttons.append(create_button (win, 110.11, 192.335, 156.585, 243.815, "3", 'lightyellow'))
    buttons.append(create_button (win, 110.11, 247.39, 156.585, 298.87, "."))
    buttons.append(create_button (win, 110.11, 302.445, 156.585, 353.925, "1/x", 'lightblue'))
    buttons.append(create_button (win, 110.11, 357.5, 156.585, 408.98, "C", 'lightblue'))
    buttons.append(create_button (win, 110.11, 412.555, 156.585, 464.035, "M+", 'lightblue'))
    buttons.append(create_button (win, 162.305, 82.225, 208.78, 133.705, "*", 'pink'))
    buttons.append(create_button (win, 162.305, 137.28, 208.78, 188.76, "/", 'pink'))
    buttons.append(create_button (win, 162.305, 192.335, 208.78, 243.815, "-", 'pink'))
    buttons.append(create_button (win, 162.305, 247.39, 208.78, 298.87, "+", 'pink'))
    buttons.append(create_button (win, 162.305, 302.445, 208.78, 353.925, "%", 'lightblue'))
    buttons.append(create_button (win, 162.305, 357.5, 208.78, 408.98, "=", 'pink'))
    buttons.append(create_button (win, 162.305, 412.555, 208.78, 464.035, "", 'pink'))


    displayString = ''
    displayTextElement = Text(Point(200, 50), "")
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
