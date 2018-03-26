
# CMPT 120 - Lab #6
# Maria Costello
# 22-03-2018

def showIntro():
       print("Welcome to the Arithmetic Engine!")
       print("=================================\n")
       print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
       print("\nThank you for using the Arithmetic Engine…")
       print("\nPlease come back again soon!")
       # fixed so that it will accept lowercase 
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmdlower = cmd.lower()
        if cmdlower == "add":
            num1, num2 = operands() # Where is this function defined?
            result = num1 + num2
        elif cmdlower == "sub":
            num1, num2 = operands()
            result = num1 - num2
        elif cmdlower == "mult":
            num1, num2 = operands()
            result = num1 * num2
        elif cmdlower == "div":
            num1, num2 = operands()
            try:
                result = num1 // num2
            except:
                print("Unable to divide by zero!")
                continue
        elif cmdlower == "quit":
            break
        else:
            print(cmdlower, "is an invalid command.")
            continue
        print("The result is " + str(result) + ".\n")
def main():
       showIntro()
       doLoop()
       showOutro()
main()
