def printboard(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("----------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("----------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def playerturn(board, player):
    while True:
        try:
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
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print (f"{player} wins")
        quit()
    elif board[0][0] ==player and board[0][1] == player and board[0][2] == player:
        print (f"{player} wins")
        quit()
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print (f"{player} wins")
        quit()
    elif board[2][0] ==player and board[2][1]== player and board[2][2] == player:
        print (f"{player} wins")
        quit()
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print (f"{player} wins")
        quit()
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print (f"{player} wins")
        quit()
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print (f"{player} wins")
        quit()
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print (f"{player} wins")
        quit()
    else:
        return

def tie(board):
    if board [0][0] != ' ' and board [1][0] != ' ' and board [2][0] != ' ' and board [0][1] != ' ' and board [1][1] != ' ' and board [2][1] != ' ' and board [0][2] != ' ' and board [1][2] != ' ' and board [2][2] != ' ':
        print ("It is a tie")
        quit()
    else:
        return


def main():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    while True:
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
            tie(board)
            win(board, player1)
            playerturn(board, player2)
            printboard(board)
            tie(board)
            win(board, player2)

main()
