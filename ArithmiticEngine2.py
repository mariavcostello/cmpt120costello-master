
# CMPT 120 - Lab #6
# YOUR NAME
# DD-MMM-YYYY
###

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
            result = num1 + num2
        elif cmdlower == "sub":
            result = num1 - num2
        elif cmdlower == "mult":
            result = num1 * num2
        elif cmdlower == "div":
            try:
                result = num1 // num2
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
