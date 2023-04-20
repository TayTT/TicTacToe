import copy
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


def choose_random(board):
    possible_moves = get_possible_moves(board)
    if possible_moves:
        return random.choice(possible_moves)


def make_move(board, player_sign, chosen_spot):
    if chosen_spot is not None and board[chosen_spot] is None:
        board[chosen_spot] = player_sign
    return board


def choose_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_possible_moves(board):
        tmp_board = copy.deepcopy(board)
        tmp_board[move] = 'X'
        score = minimax(tmp_board, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def minimax(board, is_maximizing_player):
    if is_won(board)[0]:
        return get_winning_score(board)

    if is_tie(board):
        return 0

    if is_maximizing_player:
        best_score = float('-inf')
        for move in get_possible_moves(board):
            tmp_board = copy.deepcopy(board)
            tmp_board[move] = 'X'
            score = minimax(tmp_board, False)
            best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for move in get_possible_moves(board):
            tmp_board = copy.deepcopy(board)
            tmp_board[move] = 'O'
            score = minimax(tmp_board, True)
            best_score = min(score, best_score)
        return best_score
# def choose_best_move(board):
#     best_move = None
#     tmp_board = copy.deepcopy(board)
#     for move in get_possible_moves(tmp_board):
#         tmp_board[move] = 'X'
#         if minimax(tmp_board) == 1:
#             best_move = move
#     return best_move
#
#
# def minimax(board):
#     for move in get_possible_moves(board):
#         winning_state = is_won(board)[0]
#         if winning_state:
#             return get_winning_score(board)
#         else:
#             board[choose_random(board)] = 'O'
#             if winning_state:
#                 return get_winning_score(board)
#             else:
#                 board[move] = 'X'
#                 board[choose_random(board)] = 'O'
#                 return get_winning_score(board)


# def minimax(board, is_maximizing_player):
#     if is_won(board)[0]:
#         return get_winning_score(board)
#
#     if is_tie(board):
#         return 0
#
#     if is_maximizing_player:
#         best_score = float('-inf')
#         for move in get_possible_moves(board):
#             tmp_board = copy.deepcopy(board)
#             tmp_board[move] = 'X'
#             score = minimax(tmp_board, False)
#             best_score = max(score, best_score)
#         return best_score
#
#     else:
#         best_score = float('inf')
#         for move in get_possible_moves(board):
#             tmp_board = copy.deepcopy(board)
#             tmp_board[move] = 'O'
#             score = minimax(tmp_board, True)
#             best_score = min(score, best_score)
#         return best_score


def is_tie(board):
    possible_moves = get_possible_moves(board)
    if len(possible_moves) == 0:
        return True
    else:
        return False


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


def get_winning_score(board):
    who_won = is_won(board)[0]
    if who_won == 'X':
        return 1
    elif who_won == 'O':
        return -1
    else:
        return 0

