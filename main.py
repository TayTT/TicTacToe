import play
import copy

board = [None] * 9

i = 0

while True:
    board = play.make_move(board, 'X', play.choose_best_move(board))
    [winning_state, who_won] = play.is_won(board)
    play.draw(copy.deepcopy(board))
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
    play.draw(copy.deepcopy(board))
    i += 1
    if winning_state:
        print("The game was won by ", who_won, " in ", i, "moves.")
        play.draw(board)
        break
    elif play.is_tie(board):
        print("The game is a tie. ", i, " moves were made")
        play.draw(board)
        break
