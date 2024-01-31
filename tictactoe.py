board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

depth = 9
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

    global depth

    inp = int(input("what number do ya want?"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = player
        depth -= 1
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

# Checks the final results
def whoIsWinner():

    global depth
    global winner

    if depth == 0:
        return "Tie"
    else:
        crossWin()
        verWin()
        horiWin()
        return winner

# Dictonary to check winner values
scores = {"X": -1,
          "O": 1,
          "Tie": 0}


# Algoritm to check what move is the most optimal move for the enemy bot to use, uses a minmax function
def miniMaxMove(board, aiPlayer, depth):

    global scores
    global winner

    result = whoIsWinner()
    if (result != None):
        score = scores[result]
        print(score)
        return score
    move = 0
    
    if aiPlayer:
        maxScore = -1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = miniMaxMove(board, False, depth - 1)
                board[i] = "-"
                winner = None
                if (score > maxScore):
                    maxScore = score
                    move = i
        return move
    else:
        maxScore = 1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = miniMaxMove(board, True, depth - 1)
                board[i] = "-"
                winner = None
                if (score < maxScore):
                    maxScore = score
                    move = i
        return move


# A loop that continues until the variable gameNotOver becomes false
while gameNotOver:
    createBoard(board)
    move(board)
    winner = whoIsWinner()
    if winner != None:
        createBoard(board)
        print(whoIsWinner() + " Is the winner")
        gameNotOver = False

    #Find a more efficent process
    createBoard(board)
    board[miniMaxMove(board, True, depth)] = "O"
    winner = whoIsWinner()
    print(depth)
    if winner != None:
        createBoard(board)
        print(whoIsWinner() + " Is the winner")
        gameNotOver = False