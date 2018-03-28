
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
    
def doLoop():
    
    while True:
        
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        if cmd == "quit":
            break
        else:
            try: 
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            
            except ValueError:
                print ("Must be a number!")
                continue
            
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1 * num2
            elif cmd == "div":
                if num2 == 0:
                    try:
                        frac = num1 / num2
                    except:
                        print("Unable to divide by zero")
                        continue
                result = num1 // num2
            else:
                print("That is not a valid command.")
                break
            print("The result is " + str(result) + ".\n")
            
        
def main():
    showIntro()
    doLoop()
    showOutro()
    
main()
