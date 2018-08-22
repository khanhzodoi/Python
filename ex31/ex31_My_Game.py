import os
import time
# Tic - Tac -  toe
# Plays the game of Tic-Tac-Toe against a human opponent

#global constants
X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 10


def clear():
    if os.name == 'nt':
        _ = os.system('test&cls')

    else:
        _ = os.system('clear')




def display_instruct():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-tac-toe.
    This will be a showdown between your human brain and my silicon processorself.

    You will make your move known by entering a number, 1 - 9. The number
    will correspond to the board position as illustrated:
                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ('y', 'yes', 'no', "n"):
        response = input(question)
    return response.lower()


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y" or go_first == 'yes':
        print("\n Then take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoin... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create new board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    board[0] = "Null"
    return board


def display_board(board):
    """Display game board on screen."""
    print("\n\t {} | {} | {}".format(board[1], board[2], board[3]))
    print("\t ---------")
    print("\n\t {} | {} | {}".format(board[4], board[5], board[6]))
    print("\t ---------")
    print("\n\t {} | {} | {}\n".format(board[7], board[8], board[9]))


def legal_move(board):
    """Create list of legal moves."""
    moves = []
    for square in range(1, NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (3, 6, 9),
                   (1, 5, 9),
                   (3, 5, 7))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return "TIE"
    return None

def human_move(board, human):
    """Get human move."""
    legal = legal_move(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (1 - 9):", 1, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move


def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positioms to have, in order
    BEST_MOVES = (5, 1, 3, 7, 9, 2, 4, 6, 8)

    print("I shall take square number", end=" ")
    # if computer can win, take that move
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY
    # if human can win, block that move
    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move
        board[move] = EMPTY
    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_move(board):
            print (move)
            return move

def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
                "But never again! I, the computer, so swear it!")
    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
                "But never again! I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
                "Celebrate today... for this is the best you will ever achieve.")


def main():
    clear()
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer

        time.sleep(0.65)
        clear()
        display_instruct()
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start the program
main()
input("\n\nPress the enter key to quit.")
