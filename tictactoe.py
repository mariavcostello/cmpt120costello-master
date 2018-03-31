# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Maria Costello
# Created: 2018-03-27


symbol = [ " ", "x", "o" ]
print("+-----+")
board = [
        [ " ", " ", " "],
        [ " ", " ", " "],
        [ " ", " ", " "]
        ] 
def printBoard(board):
    for row in range(3):
        for num in range(3):
            print('|',end="")
            if board[row][num] == 0:
                board[row][num] == ""
            print(board[row] [num], end="")
        print("|")
        print("+-----+")
    
def markBoard(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = symbol[player]
        return True 
    else:
        print("Try again")
        return False
def getPlayerMove():   
    row = int(input("What row would you like to input in (1-3)? "))
    column = int(input("What column would you like to input in (1-3)? "))
    return int(row) -1 , int(column) -1 
def hasBlanks(board):
    end = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == symbol[0]:
                return True
            if board[row][column] == symbol[1] or board[row][column] == symbol[2]:
                end = end + 1
                if end == 9:
                    print('')
                    return False 
def main():
   player = 1
while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if markBoard(board,row,col,player):
            player = player % 2 + 1
main()
