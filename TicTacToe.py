def main():
    board ='''
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9   
    '''
    i = 0
    win = False
    print(board)
    while (win == False):
    #X's turn and win check
        board = player_one_turn(board)
        win = win_check(board)
        i += 1
        player = 1
        if win == True:
            break

    #tie checker
        if i == 9:
            print("It's a tie!")
            quit()

    #O's turn and win check
        board = player_two_turn(board)
        win = win_check(board)
        i += 1
        player = 2

    if player == 1:
        print("X's Wins")
    elif player == 2:
        print("O's Wins")

#Player ones turn, takes player input and changes the number on the board to an X
def player_one_turn(board):
    turn = int(input(f'Player 1, type in the number corresponding to the spot you would like to play: '))
    
    if turn < 10 and turn > 0:
        turn = str(turn)
        board = board.replace(turn, 'X')
        print(board)
    return board

#Player twos turn, takes player input and changes the number on the board to an O
def player_two_turn(board):
    turn = int(input(f'Player 2, type in the number corresponding to the spot you would like to play: '))

    if turn < 10 and turn > 0:
        turn = str(turn)
        board = board.replace(turn, 'O')
        print(board)
    return board

#check after every turn to see if anyone has won yet
def win_check(board):
    b2 = list(board)
#top row win check
    if b2[5] == b2[7] and b2[5] == b2[9]:
        return True
#middle row win check
    elif b2[25] == b2[27] and b2[25] == b2[29]:
        return True
#bottom row win check
    elif b2[45] == b2[47] and b2[45] == b2[49]:
        return True
#left column win check
    elif b2[5] == b2[25] and b2[5] == b2[45]:
        return True
#middle column win check
    elif b2[7] == b2[27] and b2[7] == b2[47]:
        return True
#right column win check
    elif b2[9] == b2[29] and b2[9] == b2[49]:
        return True
#diagonal win check
    elif b2[5] == b2[27] and b2[5] == b2[49]:
        return True
#diagonal win check
    elif b2[9] == b2[27] and b2[9] == b2[45]:
        return True
    else:
        return False
main()