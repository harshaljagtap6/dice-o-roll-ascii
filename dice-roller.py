import random


def take_user_input():
    print("Press 1 to roll dice:")
    print("Press 2 to exit")
    user_choice = int(input("Enter your choice:"))
    return user_choice


def roll_dice_and_print():
    user_choice = take_user_input()
    if (user_choice == 1):
        dice_number = random.randint(1, 6)
        print(dice_number)
        if (dice_number == 1):      
            print("-----")
            print("|   |")
            print("| o |")
            print("|   |")
            print("-----")
        if (dice_number == 2):
            print("-----")
            print("|o  |")
            print("|   |")
            print("|  o|")
            print("-----")
        if (dice_number == 3):
            print("-----")
            print("|o  |")
            print("| o |")
            print("|  o|")
            print("-----")
        if (dice_number == 4):
            print("-----")
            print("|o o|")
            print("|   |")
            print("|o o|")
            print("-----")
        if (dice_number == 5):
            print("-----")
            print("|o o|")
            print("| o |")
            print("|o o|")
            print("-----")
        if (dice_number == 6):
            print("-----")
            print("|o o|")
            print("|o o|")
            print("|o o|")
            print("-----")


        
        roll_dice_and_print()

    else:
        print("(uωu 人)")
        exit


roll_dice_and_print()