# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Maria C
# Created: 2018-02-21

# JA: I only see one commit in the repository. YOu had to commit after each
# part of the lab

def main():
    # get user's first and last names
    # JA: This should had moved to a different function
    first = input("Enter your first name, all lowercase: ")
    last = input("Enter your last name, all lowercase: ")
    # TODO modify this to generate a Marist-style username
    uname = first[:10] + ('.') + last[:9] + ('1')
    # JA: You had to make it lowercase yourself
    uname = iuname.lower()
    print("Username is: ", uname)
    # ask user to create a new password
    passwd = input("Create a new password: ")
# TODO modify this to ensure the password has at least 8 characters
def passwd ():
    
   while False:
        print("Fool of a Took! That password is feeble!")
        if passwd(len) <8:
            passwd == input("Create a new password: ")

        print("The force is strong in this one…")
        if passwd(len) >8:
            print("Account configured. Your new email address is", uname + "@marist.edu")
    
main()

