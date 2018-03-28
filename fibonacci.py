#Maria Costello
#Assignment 3
#Fibonacci
# A simple program illustrating a fibonacci sequence


def main():
    x,y= 0,1
    n= eval(input("Enter a value to begin the fibonacci sequence: "))
    for i in range(n):
      x,y = y,x+y
      print(x)
    print ("Answer:",x)
    
main()
