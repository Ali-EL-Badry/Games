# File : CS112_A1_T4_Game2_20231109.py
# Purpose : Game 2 (Tic Tac Toe by numbers) player1 has odd numbers player2 has even numbers first player make a row of 
#           numbers that equal 15 win
# Author : Aly El-Deen Yasser Ali
# ID : 20231109         Section : Registration has not opened yet on College Web(S15|S16 in Future)
# Version : 4 (Final version)
# Date : 28|2|2024
# ================================================= Starting Code ======================================================

# Defining some Functions
# To print the frame
def print_tic(arr):
    for i in range(0, 3):
        for j in range(0, 3):
            print(arr[i][j], end='|')
        print()


# To check that the number player choose is 1, 2or  3 in column or row
def check_num(name, player):
    while True:
        num = input(f'{player}Select number of the {name} (1, 2 or 3): ')
        if num in ['1', '2', '3']:
            return int(num) - 1
        else:
            print('Invalid!')


# To check that each player entered a number from his array
def check_num_arr(arr):
    while True:
        print(arr)
        num = input('Enter number you select:')
        if num in arr:
            return num
        else:
            print('Invalid!')


# To check who is winner
def check_winner(arr):
    # check Two crosses equal 15 or not
    if arr[0][0] != 'x' and arr[1][1] != 'x' and arr[2][2] != 'x':
        if int(arr[0][0]) + int(arr[1][1]) + int(arr[2][2]) == 15:
            return True
    elif arr[2][0] != 'x' and arr[1][1] != 'x' and arr[0][2] != 'x':
        if int(arr[2][0]) + int(arr[1][1]) + int(arr[0][2]) == 15:
            return True

    # To check that all player have no winner row
    for i in range(0, 3):
        summition = 0
        for j in range(0, 3):
            if arr[i][j] != 'x':
                summition += int(arr[i][j])
            else:
                summition = 0
                break
        if summition == 15:
            return True
    # To check that all player have no winner column
    for i in range(0, 3):
        summition = 0
        for j in range(0, 3):
            if arr[j][i] != 'x':
                summition += int(arr[j][i])
            else:
                summition = 0
                break
        if summition == 15:
            return True

    return False


# Showing Rules For player
print("""====Tic Tac Toe by Numbers Game===
->Its Description:
==================
It look like normal game but by numbers you use numbers player one got odd 
numbers, and player 2 got even numbers you can't use the same number 2 times
first player got a column or row or cross that equal 15 wins
=============================================================================
->Its Rules:
============
1. Don't enter string or char
2. Don't enter negative number
3. Don't repeat choosing number
===============================""")

# Defining information of game
game = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
arr1 = ['1', '3', '5', '7', '9']
arr2 = ['2', '4', '6', '8', '10']
check = False

while True:

    # 1st Player 
    print_tic(game)

    while True:
        row = check_num('row', '1st player :')
        colmn = check_num('column', '1st player :')
        if game[row][colmn] == 'x':
            break
        else:
            print('Enter in an valid place!')

    numer_choosen = check_num_arr(arr1)
    game[row][colmn] = numer_choosen
    arr1.remove(numer_choosen)

    if check_winner(game):
        print('== 1st player is Winner! ==')
        check = True
        break

    # 2nd Player
    print_tic(game)

    while True:
        row = check_num('row', '2nd player :')
        column = check_num('column', '2nd player :')
        if game[row][column] == 'x':
            break
        else:
            print('Enter in an invalid place!')

    numer_choosen = check_num_arr(arr2)
    game[row][column] = numer_choosen
    arr2.remove(numer_choosen)

    if check_winner(game):
        print('== 2nd player is Winner! ==')
        check = True
        break

if not check:
    print('==Draw==')
