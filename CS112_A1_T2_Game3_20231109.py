# File : CS112_A1_T2_Game3_20231109.py
# Purpose : Game 3 (Subtract A Square) here two players play each of them must choose a square number to take it from
# pile of money and first player reach 0  win!
# Author : Aly El-Deen Yasser Ali
# ID : 20231109
# ================================================= Starting Code ======================================================
# For importation
import random


# To check that num is square of num
def check_square(num):
    if num < 0:
        return False
    elif num == 1:
        return True
    i = 1
    while i * i <= num:
        if num == i * i:
            return True
        i += 1
    return False


# To check that input is character or string
def check_string(sentence):
    while True:
        income = input(sentence)
        if income.isnumeric():
            return income
        print("Invalid Input\n====================================")


# To check the range of input
def check_range(sentence, num):
    while True:
        income = input(sentence)
        if income.isnumeric():
            if check_square(int(income)) and num - int(income) >= 0:
                return income
        print("Invalid Input\n====================================")


# Main code
# A Small Description and Showing The Rules Of The Game
print("""==Welcome To Subtract A Square Game==
Its Description:
================
There are two players that have a pile of coins(input or random).
Each player at his/her turn will choose a number of coins that is square numbers.
And so on until you reach 0 first player reach zero will win!
==================================================================================================
==================================================================================================
It's Rules:
===========
1. You have to chose only a square number of numbers like 1, 4, 9, 16, 25, 36,....
2. You can't use a fraction number
3. You cant use an string or char
4. The player who remove the last coin from the pile win
====================================================================""")

# to know what will user choose
while True:
    choice = input("""Do you want the number of coins to be random or you choose it?
[A] Random Numbers
[B] Chosen Numbers
Your choice: """).upper()
    if choice in ['A', 'B']:
        break
    print("Invalid Input")

# Getting The number of coins in pile
pile = 0
if choice == 'B':
    pile = int(check_string("Enter The Number of Coins in Pile:"))
elif choice == 'A':
    while True:
        pile = random.randint(1, 1000)
        if not check_square(pile):
            break

# Starting the game
while True:

    # player one
    print("The number of coins =", pile)
    player1 = int(check_range("Enter 1st player choice: ", pile))
    pile -= player1
    if pile == 0:
        print("===Player 1 Wins!===")
        break
    print('The coins left =', pile)
    print('=======================')

    # player Two
    player2 = int(check_range("Enter 2st player choice: ", pile))
    pile -= player2
    if pile == 0:
        print("===Player 2 Wins!===")
        break
    print('The coins left =', pile)
    print('=======================')
