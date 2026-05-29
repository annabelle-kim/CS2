  
def printboard(board):
    '''
    function that prints the game board with the location of the X's and O's

    Arguments:
        board: the list that has the layour of the board
    
    Returns:
        print: prints what the current board looks like
    '''    
    print("  1   2   3")
    print(f"1 {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" -----------")
    print(f"2 {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" -----------")
    print(f"3 {board[2][0]} | {board[2][1]} | {board[2][2]}")

def playerturn(board, player):
    '''
    lets the player take their turn in placing their X or O

    Arguments:
        player: the player who's turn it is
        board: the regular board that the game is being played on
    
    Returns:
        print: the updated board which includes the most reent turn
    '''
    while True:
        try:                                                                    #makes sure that the input is a valid and possible value
            column = int(input("Which column do you wannt to go in? ")) - 1
            row = int(input("Which row do you want to go in? ")) - 1

            if column < 0 or column > 2 or row < 0 or row > 2:
                print("Invalid Response")
                continue
        except ValueError:
            print('Integers only!')
            continue

        if board[row][column] != ' ':
            print('Enter a valid space')
            continue
        else:
            board[row][column] = player
            break

def win(board, player):
    '''
    checks to see if either of the players have won and gotten three in a row. function checks after each player takes a turn

    Arguments:
        board: the board that the game has been being played on
        player: the player whos turn it most recently was
    
    Returns:
        boolean: true or false based on whether they have a winning combination or not
    '''
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:      #all of the different winning conditions 60-83
        print (f"{player} wins")
        return True
    elif board[0][0] ==player and board[0][1] == player and board[0][2] == player:
        print (f"{player} wins")
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print (f"{player} wins")
        return True
    elif board[2][0] ==player and board[2][1]== player and board[2][2] == player:
        print (f"{player} wins")
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print (f"{player} wins")
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print (f"{player} wins")
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print (f"{player} wins")
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print (f"{player} wins")
        return True
    else:
        return
        

def tie(board):
    '''
    checks to see if the game ended in a tie where nobody wins or loses.

    Arguments:
        board: uses the board that has been played on the entire game
    
    Returns:
        boolean: true if the tie conditions match the game board
    '''    
    if board [0][0] != ' ' and board [1][0] != ' ' and board [2][0] != ' ' and board [0][1] != ' ' and board [1][1] != ' ' and board [2][1] != ' ' and board [0][2] != ' ' and board [1][2] != ' ' and board [2][2] != ' ':
        print ("It is a tie")
        return True
    else:
        return


def main():
    while True:
        board = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
        player1 = input("Do you want to be X or O: ").upper()

        if player1 == "X":
            player2 = "O"
        elif player1 == "O":
            player2 = "X"
        else:
            print("Ivalid response try again")
            continue
        printboard(board)
        
        while True:
            playerturn(board, player1)
            printboard(board)
            if win(board, player1) == True:
                break
            if tie(board) == True:
                break
            playerturn(board, player2)
            printboard(board)
            if win(board, player2) == True:
                break
        
        while True:
            play_again = input("Do you want to play again? ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                quit()
            else:
                print("Invalid Response")
        


main()
