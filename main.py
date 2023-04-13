import play

board = [None, None, None,
         None, None, None,
         None, None, None]

play.draw(board)

player = 'X'
for i in range(10):
    print("Move ", i+1)
    board = play.make_move(board, player, play.choose_random(board))
    # print("Empty spots: ", play.get_empty_spots(board))
    # if player == "X":
    #     player = "0"
    # elif player == "0":
    #     player = "X"
    player = '0' if player == 'X' else 'X'
    play.draw(board)
    [winning_state, who_won] = play.is_won(board)
    if winning_state:
        print("The game is won by ", who_won)
        break
    elif play.is_tie(board):
        print("The game is a tie.")
        break
