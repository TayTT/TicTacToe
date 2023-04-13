from random import random


def draw(current_board):
    print("| ", current_board[0], " | ", current_board[1], " | ", current_board[2])
    print("-----------------------")
    print("| ", current_board[3], " | ", current_board[4], " | ", current_board[5])
    print("-----------------------")
    print("| ", current_board[6], " | ", current_board[7], " | ", current_board[8])


def get_empty_spots(board):
    empty_spots = []
    for i in board:
        if board(i) is None:
            empty_spots.append(i)
    return empty_spots


def is_won(board):
    # check rows
    if board[0] == board[1] == board[2] is not None:
        return True, board[0]
    elif board[3] == board[4] == board[5] is not None:
        return True, board[3]
    elif board[6] == board[7] == board[8] is not None:
        return True, board[6]

    # check columns
    elif board[0] == board[3] == board[6] is not None:
        return True, board[0]
    elif board[1] == board[4] == board[7] is not None:
        return True, board[1]
    elif board[2] == board[5] == board[8] is not None:
        return True, board[2]

    # check diagonals
    elif board[0] == board[4] == board[8] is not None:
        return True, board[0]
    elif board[2] == board[4] == board[6] is not None:
        return True, board[2]

    else:
        return False


def choose_random(board):
    return random.randint(0, len(board.get_empty_spots))


def make_move(board, player_sign, chosen_spot):
    if chosen_spot is None:
        board[chosen_spot] = player_sign
    return board
