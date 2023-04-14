import play

board = [None] * 9

player = 'X'
for i in range(10):
    board = play.make_move(board, player, play.choose_random(board))
    player = 'O' if player == 'X' else 'X'
    [winning_state, who_won] = play.is_won(board)
    if winning_state:
        print("The game was won by ", who_won, " in ", i+1, "moves.")
        play.draw(board)
        break
    elif play.is_tie(board):
        print("The game is a tie. ", i+1, " moves were made")
        play.draw(board)
        break
