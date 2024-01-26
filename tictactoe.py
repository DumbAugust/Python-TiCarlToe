board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

player = "X"
winner = None
gameNotOver = True 

def createBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def move(board):
    inp = int(input("what number do ya want?"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = player
    else:
        print("pick another")


def horiWin():
    global winner
    for i in [0, 3, 6]:
        if board[i] == board[i + 1] == board[i + 2] != "-":
            winner = board[i]

def verWin():
    global winner
    for i in [0, 1, 2]:
        if board[i] == board[i + 3] == board[i + 6] != "-":
            winner = board[i]

def crossWin():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    if board[6] == board[4] == board[2] != "-":
        winner = board[6]

def aiMove(board):
    bestScore = -10000
    for i in range(9):
        if board[i] == "-":
            score = minimax(board)
            if (score > bestScore):
                bestScore = score
                move = i
    board[move] = "O"


def miniMax(board):




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