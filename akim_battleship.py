import os
import time

def printboard(board):
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
    print(f"{player}'s board")
    printboard(board)
    dots=4
    for i in range(4):
        print(f"You have {dots} boat(s) left to place")
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
            print("Go again!")
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



'''def win(realboard):
    for spot in realboard:
        if spot == ("🛳️"):
        '''



def main():
    player1 = input("What is Player 1's name? ")
    player2 = input("What is Player 2's name? ")

    
    while True:
        score1 = 0
        score2= 0
        realboard1 = [[' ', ' ', ' ', ' ', ' '],
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
                print(f"{player1} wins!")
                playagain= input("Do you want to play again? ").lower()
                if playagain == "yes":
                    break
                else:
                    quit()
            player2win,score2=player_turn(player2, realboard1, guessboard2, score2)
            if player2win:
                print(f"{player2} wins!")
                playagain= input("Do you want to play again? ").lower()
                if playagain == "yes":
                    break
                else:
                    quit()
        break
        

main()
