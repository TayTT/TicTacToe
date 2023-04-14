import random


def draw(current_board):
    for i in range(len(current_board)):
        if current_board[i] is None:
            current_board[i] = ' '
    print("| ", current_board[0], " | ", current_board[1], " | ", current_board[2], " |")
    print("-------------------")
    print("| ", current_board[3], " | ", current_board[4], " | ", current_board[5], " |")
    print("-------------------")
    print("| ", current_board[6], " | ", current_board[7], " | ", current_board[8], " |")
    print(" ")


def get_possible_moves(board):
    possible_moves = []
    for i in range(len(board)):
        if board[i] is None:
            possible_moves.append(i)
    return possible_moves


def is_tie(board):
    possible_moves = get_possible_moves(board)
    if len(possible_moves) == 0:
        return True
    else:
        return False


def choose_random(board):
    possible_moves = get_possible_moves(board)
    if possible_moves:
        return random.choice(possible_moves)


def make_move(board, player_sign, chosen_spot):
    if board[chosen_spot] is None:
        board[chosen_spot] = player_sign
    return board


def is_won(board):
    # check rows
    if board[0] == board[1] == board[2] is not None:
        return [True, board[0]]
    elif board[3] == board[4] == board[5] is not None:
        return [True, board[3]]
    elif board[6] == board[7] == board[8] is not None:
        return [True, board[6]]

    # check columns
    elif board[0] == board[3] == board[6] is not None:
        return [True, board[0]]
    elif board[1] == board[4] == board[7] is not None:
        return [True, board[1]]
    elif board[2] == board[5] == board[8] is not None:
        return [True, board[2]]

    # check diagonals
    elif board[0] == board[4] == board[8] is not None:
        return [True, board[0]]
    elif board[2] == board[4] == board[6] is not None:
        return [True, board[2]]

    else:
        return [False, "no one"]

#
# def is_over(board):
#     [state, who] = is_won(board)
#     if state or is_tie(board):
#         return True
#     else:
#         return False


def get_winning_score(board):
    [winning_state, who_won] = is_won(board)
    if who_won == 'X':
        return 1
    elif who_won == 'O':
        return -1
    else:
        return 0


def minimax(board):
    #  checking if the game is over
    # [winning_state, who_won] = is_won(board)
    # if winning_state:
    #     print("The game was won by ", who_won)
    #     draw(board)
    #     return
    # elif is_tie(board):
    #     print("The game is a tie. ")
    #     draw(board)
    #     return
    for move in get_possible_moves(board):
        [winning_state, who_won] = is_won(board)
        if winning_state:
            return get_winning_score(board)
        else:
            board[move] = 'X'
            board[choose_random(board)] = 'O'
            minimax(board)

    