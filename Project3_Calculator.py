#Maria Costello
#Project 3 Scientific
#March-29-2018

from graphics import *
from button import Button
import math

class Calculator:
    def __init__(self):
        win = GraphWin("calculator", 350, 350)
        win.setCoords(0,0,10,27)   
        win.setBackground("orange")
        self.win = win
        self.__createButtons()
        self.__createDisplayEq()
        self.__createMemBox()
        self.__createDisplayAn()
        self.memory = "0"
        
    def __createButtons(self):
        bSpecs = [(2,21,"MC"), (3.5,21,"M+"), (5,21,"MS"), (6.5,21,"M-"), (8,21,"MR"),
                  (2,18,"("), (3.5,18,")"), (5,18,"%"), (6.5,18,"**2"), (8,18,"**0.5"),
                  (2,15,"7"), (3.5,15,"8"), (5,15,"9"), (6.5,15,"<-"), (8,15,"1/x"),
                  (2,12,"4"), (3.5,12,"5"), (5,12,"6"), (6.5,12,"*"), (8,12,"/"),
                  (2,9,"1"), (3.5,9,"2"), (5,9,"3"), (6.5,9,"+"), (8,9,"-"),
                  (2,6,"C"), (3.5,6,"0"), (5,6,"."), (6.5,6,"SCI")]
        self.buttons = []
        
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))
        self.buttons.append(Button(self.win,Point(8,6),1.55,2.5,"="))
        for b in self.buttons:  b.activate()

    def __createSciButtons(self):
        bSpecs = [(2,21,"MC"), (3.5,21,"M+"), (5,21,"MS"), (6.5,21,"M-"), (8,21,"MR"),
                  (2,18,"("), (3.5,18,")"), (5,18,"%"), (6.5,18,"**2"), (8,18,"**0.5"),
                  (2,15,"7"), (3.5,15,"8"), (5,15,"9"), (6.5,15,"<-"), (8,15,"1/x"),
                  (2,12,"4"), (3.5,12,"5"), (5,12,"6"), (6.5,12,"*"), (8,12,"/"),
                  (2,9,"1"), (3.5,9,"2"), (5,9,"3"), (6.5,9,"+"), (8,9,"-"),
                  (2,6,"C"), (3.5,6,"0"), (5,6,"."), (6.5,6,"SCI"), (2,3,"sin"), (3.5,3,"cos"), (5,3,"tan"), (6.5,3,"arcsin"), (8,3,"arccos"),
                    (2,1,"artan"), (3.5,1,"log"), (6,1,"ln"), (7.5,1,"10**x"), (8,1,"x**y")]
        self.buttons = []
        
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))
        self.buttons.append(Button(self.win,Point(8,6),1.5,2.5,"="))
        for b in self.buttons:  b.activate()
        
    def __createMemBox(self):
        bg = Rectangle(Point(1.5,24), Point(1.5,26))   
        bg.setFill("lightblue")
        bg.draw(self.win)
        text = Text(Point(1,12.25), "")  
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("normal")
        text.setSize(12)
        self.M = text
        self.eqflag = False
        
    def __createDisplayEq(self):
        bg = Rectangle(Point(1,25), Point(9,27))
        bg.setFill("lightblue")
        bg.draw(self.win)
        text = Text(Point(4,26), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("normal")
        text.setSize(12)
        self.display = text

    def __createDisplayAn(self):
        bg = Rectangle(Point(1,23), Point(9,25))
        bg.setFill('lightblue')
        bg.draw(self.win)
        text = Text(Point(4,24), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("normal")
        text.setSize(12)
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
            self.eqflag=False
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
            y = eval(input("Enter a y value"))
            result = (eval(text))** y
            self.display2.setText(str(result))
            
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)
            
if __name__ == '__main__':
    theCalc = Calculator()
    theCalc.run()
