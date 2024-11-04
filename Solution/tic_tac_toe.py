import numpy as np

# Initialize a 3x3 board with zeros
board = np.zeros((3, 3), dtype=int)

# Display board with X, O, or space if empty for each cell
def display_board():

    print("\n\t0\t1\t2")

    # I represented X by 1 and O by -1 to simplify the evaluation of the board using sums
    symb = {1: "\tX", -1: "\tO", 0: "\t"}

    for i in range(3):
        print(f"{i} " + " ".join(symb[board[i, j]] for j in range(3)))


def check_win():
    # Check rows and columns
    for i in range(3):
        if board[i].sum() == 3:
            return 'X'
        elif board[i].sum() == -3:
            return 'O'

        if board[:, i].sum() == 3:
            return 'X'
        elif board[:, i].sum() == -3:
            return 'O'

    # Check diagonals
    if np.trace(board) == 3:
        return 'X'
    elif np.trace(board) == -3:
        return 'O'

    if np.trace(np.fliplr(board)) == 3:
        return 'X'
    elif np.trace(np.fliplr(board)) == -3:
        return 'O'

# A draw happens if there is no winner and the board is full
def check_draw():
    board_full = True

    # if there is a winner there is no draw
    winner = check_win()
    if winner is not None:
        board_full = False
        return board_full

    for row in board:
        for cell in row:
            if cell == 0:
                board_full = False
                break
        if not board_full:
            break

    return board_full

def make_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as coordinates (two numbers separated by a comma, like this: 0,2)\t:")
            row, col = map(int, move.split(","))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Please enter a valid move (values between 0 and 2)")
                continue

            if board[row, col] != 0:
                print("Cell is already occupied. Choose another cell")
                continue

            board[row, col] = 1 if player == "X" else -1
            break

        except ValueError:
            # Handle invalid input format
            print("Invalid input ! Please enter two numbers separated by a space")


def main():
    current_player = "X"
    game_over = False

    # Game loop
    while not game_over:
        # Display the current board
        display_board()

        # Ask the current player to make a move
        make_move(current_player)

        # Check if the current player has won
        winner = check_win()
        if winner:
            display_board()
            print(f"Player {winner} wins!")
            game_over = True
            continue

        # Check if the game is a draw
        if check_draw():
            display_board()
            print("It's a draw!")
            game_over = True
            continue

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
