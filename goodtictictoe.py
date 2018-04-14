symbol = [ " ", "x", "o" ]


def printBoard(board):
    print('+-----------+')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('+-----------+')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('+-----------+')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('+-----------+')
    


def markBoard(board,player):
    board = player
    pass

def getPlayerMove():
    board = int(input ("Please enter a number 0 to 8.")
    return(board)

def hasBlanks(board):
    for i in range(8):
        for k in range(8):
            if board[i][k]==0:
                return True
    return False

def main():
    player = 1
    while hasBlanks(board):
        printBoard(board)
        board = getPlayerMove()
        markBoard(board,player)
        player = player % 2 + 1
main()
