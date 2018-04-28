
#Project 5
#Maria Costello
#Prof. Arias
#April-25-2018

from graphics import *

from button import Button

import math

class Calculator:

    def __init__(self):

        win = GraphWin("calculator", 310, 355)

        win.setCoords(0,0,10,27)   

        win.setBackground("orange")

        self.win = win

        self.__createButtons()

        self.__createDisplayEq()

        self.__createMemBox()

        self.__createDisplayAn()

        self.memory = "0"

        

    def __createButtons(self):

        bSpecs = [(1,19,"MC"), (3,19,"M+"), (5,19,"MS"), (7,19,"M-"), (9,19,"MR"),

                  (1,16,"("), (3,16,")"), (5,16,"%"), (7,16,"**2"), (9,16,"**0.5"),

                  (1,13,"7"), (3,13,"8"), (5,13,"9"), (7,13,"<-"), (9,13,"1/x"),

                  (1,10,"4"), (3,10,"5"), (5,10,"6"), (7,10,"*"), (9,10,"/"),

                  (1,7,"1"), (3,7,"2"), (5,7,"3"), (7,7,"+"), (9,7,"-"),

                  (1,4,"C"), (3,4,"0"), (5, 4,"."), (7,4,"SCI")]

        self.buttons = []

        

        for cx,cy,label in bSpecs:

            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))

        self.buttons.append(Button(self.win,Point(9,4),1.5,2.5,"="))

        for b in self.buttons:  b.activate()



    def __createSciButtons(self):

        bSpecs = [(1,19,"MC"), (3,19,"M+"), (5,19,"MS"), (7,19,"M-"), (9,19,"MR"),

                  (1,16,"("), (3,16,")"), (5,16,"%"), (7,16,"**2"), (9,16,"**0.5"),

                  (1,13,"7"), (3,13,"8"), (5,13,"9"), (7,13,"<-"), (9,13,"1/x"),

                  (1,10,"4"), (3,10,"5"), (5,10,"6"), (7,10,"*"), (9,10,"/"),

                  (1,7,"1"), (3,7,"2"), (5,7,"3"), (7,7,"+"), (9,7,"-"),

                  (1,4,"C"), (3,4,"0"), (5,4,"."), (7,4,"SCI"), (11,19,"sin"), (11,16,"cos"), (11,13,"tan"), (11,10,"arcsin"), (11,7,"arccos"),

                    (1,1,"arctan"), (3,1,"log"), (5,1,"ln"), (7,1,"10**x"), (9,1,"x**y")]

        self.buttons = []

        

        for cx,cy,label in bSpecs:

            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))

        self.buttons.append(Button(self.win,Point(11,4),1.5,2.5,"="))

        for b in self.buttons:  b.activate()

        

    def __createMemBox(self):

        bg = Rectangle(Point(1.5,24), Point(1.5,26))   

        bg.setFill("yellow")

        bg.draw(self.win)

        text = Text(Point(2,12.25), "")  

        text.draw(self.win)

        text.setFace("courier")

        text.setStyle("normal")
        text.setSize(14)

        self.M = text

        self.eqflag = False

        

    def __createDisplayEq(self):

        bg = Rectangle(Point(.5,23), Point(7.5,26))

        bg.setFill("pink")

        bg.draw(self.win)
        

        text = Text(Point(5,25.5), "")

        text.draw(self.win)

        text.setFace("courier")

        text.setStyle("normal")

        text.setSize(14)

        self.display = text



    def __createDisplayAn(self):

        bg = Rectangle(Point(.5,21.5), Point(7.5,24))

        bg.setFill('light Blue')

        bg.draw(self.win)

        text = Text(Point(5,23), "")

        text.draw(self.win)

        text.setFace("courier")

        text.setStyle("normal")

        text.setSize(14)

        self.display2 = text

        

    def getButton(self):

        while True:

            p = self.win.getMouse()

            for b in self.buttons:

                if b.clicked(p):

                    return b.getLabel()

                

    def processButton(self, key):

        text = self.display.getText()

        innumber=text and text[-1].isdigit()

        result = 0

        print (key)

        if key == "C":

            self.display.setText("")

            self.display2.setText("")

            self.eqflag = True

            return

        elif key == "<-":

            self.display.setText(text[:-1])

            return

        elif key == "=":

            try:

                result = eval(text)

            except:

                result = "Error"

            self.display2.setText(str(result))

            print ("Result",result)

            self.eqflag = True

            return

        if key == "MR":

            if not innumber:

                self.display.setText(text+self.memory)

            else: self.display.setText(self.memory)

        elif key == "MC":

            self.memory = "0"

            self.M.setText('')

        elif key == "MS":

            self.memory = text or "0"

            if self.memory != "0":

                self.M.setText("M")

        elif key == "M+":

            self.memory = str(eval(text + "+" + str(self.memory)))

            if self.memory != '0':

                self.M.setText("M")

        elif key == "M-":

            self.memory = str(eval(text + "-" +str(self.memory)))

            if self.memory != '0':

                self.M.setText("M")

        elif key == "1/x":

            try:

                result = 1/(int(text))

            except:

                result = "Error"

            self.display.setText(str(result))

        elif key == "x**2":

            result = int(text)**2

            self.display.setText(str(result))

        else:

            if not self.eqflag or not key.isdigit():

                self.display.setText(text + key)

            else:

                self.display.setText(key)

            self.eqflag = False

        if key == "SCI":

            self.__createSciButtons()

            self.display.setText(text[:-1])

        if key == "sin":

            result = math.sin(eval(text))

            self.display2.setText(str(result))

        elif key == "cos":

            result = math.cos(eval(text))

            self.display2.setText(str(result))

        elif key == "tan":

            result = math.tan(eval(text))

            self.display2.setText(str(result))

        elif key == "arcsin":

            result = math.asin(eval(text))

            self.display2.setText(str(result))

        elif key == "arccos":

            result = math.acos(eval(text))

            self.display2.setText(str(result))

        elif key == "arctan":

            result = math.atan(eval(text))

            self.display2.setText(str(result))

        elif key == "log":

            result = math.log10(eval(text))

            self.display2.setText(str(result))

        elif key == "ln":

            result = math.log(eval(text))

            self.display2.setText(str(result))

        elif key == "10**x":

            result = 10**(eval(text))

            self.display2.setText(str(result))

        elif key == "x**y":

            y = eval(input("Please enter a y value"))

            result = (eval(text))** y

            self.display2.setText(str(result))

            

    def run(self):

        while True:

            key = self.getButton()

            self.processButton(key)

            

if __name__ == '__main__':

    theCalc = Calculator()

    theCalc.run()
