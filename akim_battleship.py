import os
import time

def printboard(board):
    '''
    print the gameboard and its values

    Arguments:
        board: which board the code is using 
    
    Returns:
        print: prints what the current board looks like
    '''
    print("  1   2   3   4   5")
    print(f"1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}")
    print(" --------------------")
    print(f"2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}")
    print(" ---------------------")
    print(f"3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}")
    print(" ---------------------")
    print(f"4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}")
    print(" ---------------------")
    print(f"5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}")

def place_dots(player, board):
    '''
    place the 4 boats onto the gameboard

    Arguments:
        player: the player who is placing thier ships
        board: the board of the player who is placing their ships
    
    Returns:
        print: prints the board with the bots after each one is placed
    '''
    print(f"{player}'s board")
    printboard(board)
    dots=4
    for i in range(4):
        print(f"You have {dots} boat(s) left to place")
        while True:
            try:                                                                    #test to see if the user's input is a valid and possible value within the gameboard's guidelines
                column = int(input("Which column do you want to go in? ")) - 1
                row = int(input("Which row do you want to go in? ")) - 1

                if column < 0 or column > 4 or row < 0 or row > 4:
                    print("Invalid Response")
                    continue
            except ValueError:
                print('Integers only!')
                continue

            if board[row][column] != (' '):
                print('Enter a valid space')
                continue
            else:
                board[row][column] = ("🛳️")
                break
        dots = dots-1
    printboard(board)
    time.sleep(3)
    os.system("cls")



def player_turn(player, realboard, guessboard,score):
    '''
    general function where the player guesses where the boats of the other player are. There is also a check win code within this function.

    Arguments:
        player: which player is the one guessing
        realboard: the board with the real location of the boats of the other player
        guessboard: the board that records and has all of the guesses of the player
        score: the counter for how many boats the player has sunken
    
    Returns:
        print: prints what the current board looks like
    '''
    print(f"{player}'s turn")
    while True:
        try:
            column = int(input("Which column do you want to go in? ")) - 1
            row = int(input("Which row do you want to go in? ")) - 1

            if column < 0 or column > 4 or row < 0 or row > 4:
                print("Invalid Response")
                continue
            
        except ValueError:
            print('Integers only!')
            continue

        if guessboard[row][column] == ('💥') or guessboard[row][column] == ('❌'):
            print('Enter a valid space')
            continue
        elif realboard[row][column] == ("🛳️"):
            guessboard[row][column] = ('💥')
            score +=1
            printboard(guessboard)
            if score == 4:
                break
            print("Go Again!")
            continue

            
        else:
            guessboard[row][column] = ("❌")
            break
    printboard(guessboard)
    if score == 4:
        print(f"{player} wins!")
        return True,score
    else:
        return False,score




def main():
    player1 = input("What is Player 1's name? ")
    player2 = input("What is Player 2's name? ")

    
    while True:
        score1 = 0
        score2= 0
        realboard1 = [[' ', ' ', ' ', ' ', ' '],      #the foundational layout for the empty game boards
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ']]
        realboard2 = [[' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ']]
        guessboard1 = [[' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ']]
        guessboard2 = [[' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ']]
        place_dots(player1, realboard1)
        place_dots(player2, realboard2)
        while True:
            player1win,score1=player_turn(player1, realboard2, guessboard1, score1)
            if player1win:
                playagain= input("Do you want to play again? ").lower()
                if playagain == "yes":
                    break
                else:
                    quit()
            player2win,score2=player_turn(player2, realboard1, guessboard2, score2)
            if player2win:
                playagain= input("Do you want to play again? ").lower()
                if playagain == "yes":
                    break
                else:
                    quit()
        break
        

main()
