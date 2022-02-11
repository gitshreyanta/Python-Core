"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 15:00:00
Title : Tic-Tac-ToeGame Program
"""
#global variables
import random
board=["-", "-", "-",
       "-", "-", "-", 
       "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    """
     Description:
         Function is used to print the tic tac toe  board.
     Parameter:
        board is used.
     Return:
         Returns nothing, prints the tic tac toe board
    """
    print(board[0]+" | "+board[1]+" | "+board[2]) 
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8]) 

def playerInput(board):
    """
     Description:
         Function is used to take the user input.
     Parameter:
        board is used.
     Return:
         Returns nothing
    """
    user_input = int(input("Enter a number 1-9:"))
    if user_input >=1 and user_input <=9 and board[user_input-1] == "-":
        board[input-1] = currentPlayer
    else:
        print("Please choose another value the spot is already filled: ")    
        playerInput(board)

def checkHorizontal(board):
    """
     Description:
         Function is used to check the board horizontal.
     Parameter:
        board is used.
     Return:
         Returns the horizontal match as boolean value.
    """
    global winner 
    if board[0] == board[1] == board[2] and  board[1] != "-":
        winner = board[1] 
        return True
    elif board[3] == board[4] == board[5] and  board[3] != "-":
        winner = board[3]
        return True   
    elif board[6] == board[7] == board[8] and  board[6] != "-":
        winner = board[6]  
        return True

def checkVertical(board):
    """
     Description:
         Function is used to check the board Vertical.
     Parameter:
        board is used.
     Return:
         Returns the  vertical match as boolean value
    """
    global winner 
    if board[0] == board[3] == board[6] and  board[0] != "-":
        winner = board[0] 
        return True
    elif board[1] == board[4] == board[7] and  board[4] != "-":
        winner = board[4]
        return True   
    elif board[2] == board[5] == board[8] and  board[8] != "-":
        winner = board[8]  
        return True 

def checkDiagonal(board):
    """
     Description:
         Function is used to check the board diagonal.
     Parameter:
        board is used.
     Return:
         Returns the diagonal match as boolean value
    """
    global winner 
    if board[0] == board[4] == board[8] and  board[0] != "-":
        winner = board[0] 
        return True
    elif board[2] == board[4] == board[6] and  board[4] != "-":
        winner = board[4]
        return True 

def checkTie(board):
    """
     Description:
         Function is used to check the Tie condition.
     Parameter:
        board is used.
     Return:
         Returns nothing, prints Tie condition.
    """
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    """
     Description:
         Function is used to check the winner.
     Parameter:
        parameter is not used.
     Return:
         Returns nothing, prints the winner and board
    """
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        printBoard(board)
        gameRunning = False

        
def switchPlayer():
    """
     Description:
         Function is used to Switch between two player.
     Parameter:
        Parameter is not used.
     Return:
         Returns nothing.
    """
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    """
     Description:
         Function is used to create a computer player with random function.
     Parameter:
        board is used.
     Return:
         Returns nothing
    """
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()       

if __name__ == "__main__":    
    while  gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)























                                  