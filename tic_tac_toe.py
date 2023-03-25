import random

# Create the game board as a 3x3 matrix
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Define a function to display the game board
def display_board(board):
    print("   1   2   3")
    print("1: {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
    print("  ---|---|---")
    print("2: {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print("  ---|---|---")
    print("3: {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))

# Define a function to check if a player has won
def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        elif (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    elif (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    else:
        return False

# Define a function to play the game
def play_game():
    # Choose who goes first
    player = random.choice(["X", "O"])
    print(f"{player} goes first.")
    display_board(board)

    # Play the game until someone wins or the board is full
    while True:
        # Get the player's move
        row = int(input("Enter row number (1-3): "))
        col = int(input("Enter column number (1-3): "))
        if (board[row-1][col-1] == " "):
            board[row-1][col-1] = player
        else:
            print("That space is already taken. Try again.")
            continue

        # Display the updated game board
        display_board(board)

        # Check if the player has won
        if (check_win(board, player)):
            print(f"{player} wins!")
            break

        # Check if the board is full (i.e., a tie)
        if (all([space != " " for row in board for space in row])):
            print("It's a tie!")
            break

        # Switch to the other player
        player = "X" if player == "O" else "O"
        print(f"{player}'s turn.")

# Start the game
play_game()
