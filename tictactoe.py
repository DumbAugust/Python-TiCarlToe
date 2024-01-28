board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


player = "X"
winner = None
gameNotOver = True 

# Displays the board in the terminal
def createBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function that takes a number input and places a X on the tictactoe grid according to your choosen number
# Uses recursion if to repeat the function untill the player chooses a number which is not taken.
def move(board):
    inp = int(input("what number do ya want?"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = player
    else:
        print("pick another")
        move(board)

# Checks if all variables in a horizontal row is the same, if they are a winner is defined
def horiWin():
    global winner
    for i in [0, 3, 6]:
        if board[i] == board[i + 1] == board[i + 2] != "-":
            winner = board[i]

# Checks if all variables in a vertical row is the same, if they are a winner is defined
def verWin():
    global winner
    for i in [0, 1, 2]:
        if board[i] == board[i + 3] == board[i + 6] != "-":
            winner = board[i]

# Checks if all variables in a cross row is the same, if they are a winner is defined
def crossWin():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    if board[6] == board[4] == board[2] != "-":
        winner = board[6]

# Algoritm to check what move is the most optimal move for the enemy bot to use, uses a minmax function
def aiMove(board):
    bestScore = -10000
    for i in range(9):
        if board[i] == "-":
            score = minMax(board)
            if (score > bestScore):
                bestScore = score
                move = i
    board[move] = "O"

# The minMax function used in the aiMove function to calculate which move is the best.
def minMax(board):
    return 1

# A infinite loop that continues untill a winner is defined
while gameNotOver:
    createBoard(board)
    move(board)
    horiWin()
    verWin()
    crossWin()
    if winner != None:
        createBoard(board)
        print(winner + " Is the winner")
        gameNotOver = False
        createBoard(board)

    #Find a more efficent process
    createBoard(board)
    aiMove(board)
    horiWin()
    verWin()
    crossWin()
    if winner != None:
        createBoard(board)
        print(winner + " Is the winner")
        gameNotOver = False