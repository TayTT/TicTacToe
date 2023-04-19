import play

board = [None] * 9

# player_sign = 'X'
# for i in range(10):
#     board = play.make_move(board, player_sign, play.choose_random(board))
#     player_sign = 'O' if player_sign == 'X' else 'X'
#     [winning_state, who_won] = play.is_won(board)
#     if winning_state:
#         print("The game was won by ", who_won, " in ", i+1, "moves.")
#         play.draw(board)
#         break
#     elif play.is_tie(board):
#         print("The game is a tie. ", i+1, " moves were made")
#         play.draw(board)
#         break

# for i in range(5):
#     board = play.make_move(board, 'X', play.choose_best_move(board))
#     board = play.make_move(board, 'O', play.choose_random(board))
#     [winning_state, who_won] = play.is_won(board)
#     if winning_state:
#         print("The game was won by ", who_won, " in ", i+1, "moves.")
#         play.draw(board)
#         break
#     elif play.is_tie(board):
#         print("The game is a tie. ", i+1, " moves were made")
#         play.draw(board)
#         break

board = [None] * 9
i = 0

while True:
    board = play.make_move(board, 'X', play.choose_best_move(board))
    [winning_state, who_won] = play.is_won(board)
    i += 1
    if winning_state:
        print("The game was won by ", who_won, " in ", i, "moves.")
        play.draw(board)
        break
    elif play.is_tie(board):
        print("The game is a tie. ", i, " moves were made")
        play.draw(board)
        break
    board = play.make_move(board, 'O', play.choose_random(board))
    [winning_state, who_won] = play.is_won(board)
    i += 1
    if winning_state:
        print("The game was won by ", who_won, " in ", i, "moves.")
        play.draw(board)
        break
    elif play.is_tie(board):
        print("The game is a tie. ", i, " moves were made")
        play.draw(board)
        break
