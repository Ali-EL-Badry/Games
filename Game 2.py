print('welcome to Number scrabble')

# set the list and list_player1 and list_player2
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_player1 = []
list_player2 = []

# game playing
while len(list_player1) < 3 and len(list_player2) < 3:
    print(num_list)

    # Player 1's turn
    while True:
        try:
            num_player1 = int(input("player1:choose number from the list: "))
            break
        except ValueError:
            print("Invalid input!")

    while True:
        if num_player1 in num_list:
            list_player1.append(num_player1)
            print("List of Player 1:", list_player1)
            num_list.remove(num_player1)
            print('Remaining numbers:', num_list)
            break
        else:
            while True:
                try:
                    num_player1 = int(input("The number you entered is not in the list, choose number from the list: "))
                    break
                except ValueError:
                    print("Invalid")

    # Player 2's turn
    while True:
        try:
            num_player2 = int(input("player2:choose number from the list: "))
            break
        except ValueError:
            print("Invalid input!")

    while True:
        if num_player2 in num_list:
            list_player2.append(num_player2)
            print("List of Player 2:", list_player2)
            num_list.remove(num_player2)
            print('Remaining numbers:', num_list)
            break
        else:
            while True:
                try:
                    num_player2 = int(input("The number you entered is not in the list, choose number from the list: "))
                    break
                except ValueError:
                    print("Invalid")
# check the winner
check1 = False
check2 = False
sum_list1_numbers = sum(list_player1)
sum_list2_numbers = sum(list_player2)
if sum_list1_numbers == 15 and sum_list2_numbers == 15:
    print("the game is draw")
elif sum_list1_numbers == 15 and sum_list2_numbers != 15:
    print("player1 is winning")
elif sum_list2_numbers == 15 and sum_list1_numbers != 15:
    print("player2 is winning")
else:

    while True:
        # ==================================player 1===========================================
        print(num_list)
        while True:
            try:
                num_player1 = int(input("player1:choose number from the list: "))
                break
            except ValueError:
                print("Invalid input!")

        while True:
            if num_player1 in num_list:
                list_player1.append(num_player1)
                print("List of Player 1:", list_player1)
                num_list.remove(num_player1)
                print('Remaining numbers:', num_list)
                check1 = False
                for i in range(0, len(list_player1)):
                    for j in range(0, len(list_player1)):
                        for k in range(0, len(list_player1)):
                            if i != j and i != k and k != j:
                                if list_player1[i] + list_player1[j] + list_player1[k] == 15:
                                    print("player1 is winner!")
                                    check1 = True
                                    break
                        if check1:
                            break
                    if check1:
                        break
                break
            else:
                while True:
                    try:
                        num_player1 = int(
                            input("The number you entered is not in the list, choose number from the list: "))
                        break
                    except ValueError:
                        print("Invalid")
        if check1:
            break

        if not num_list:
            break
        # ====================================================================================
        # ========================================player 2====================================
        while True:
            try:
                num_player2 = int(input("player2:choose number from the list: "))
                break
            except ValueError:
                print("Invalid input!")

        while True:
            if num_player2 in num_list:
                list_player2.append(num_player2)
                print("List of Player 2:", list_player2)
                num_list.remove(num_player2)
                check2 = False
                print('Remaining numbers:', num_list)
                for i in range(0, len(list_player2)):
                    for j in range(0, len(list_player2)):
                        for k in range(0, len(list_player2)):
                            if i != j and i != k and j != k:
                                if list_player2[i] + list_player2[j] + list_player2[k] == 15:
                                    print("player2 is winning")
                                    check2 = True
                                    break
                        if check2:
                            break
                    if check2:
                        break
                break
            else:
                while True:
                    try:
                        num_player2 = int(
                            input("The number you entered is not in the list, choose number from the list: "))
                        break
                    except ValueError:
                        print("Invalid")
        if check2:
            break

if not check1 and not check2:
    print("the game is draw")
