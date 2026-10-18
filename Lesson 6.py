# We started from reminders from last
from random import randint


def mar():
    print("מרום הגבר")


def is_even(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


def msh(size):
    for rows in range(size + 1):
        for cols in range(rows):
            print("*", end="")
        print()


def bigger(a, b):
    print("The answer is: ")
    if a > b:
        print(f"{a} is bigger than {b}")
    elif b > a:
        print(f"{b} is bigger than {a}")
    else:
        print(f"numbers are even: {a}={b}")
    print("--------------------------------------------------+------------------------------")


# bigger(10, 5)
# msh(5)
# value = is_even()
# print(value)
# mar()


# --------------------------------------משחק אבן נייר ומספריים----------------------------

def welcome_game():  # f1
    print()
    print()
    print("========================================================")
    print("Welcome to Tal's Rock/Paper/Scissors Game (:")
    print("========================================================")
    print()


def player_name_input():  # f2
    return input("Please enter player's name: ")


def player_choice_game(player_name):
    print(f"{player_name},\nplease pick your choice:\n0. Rock\n1. Paper\n2. Scissors")
    choice = input("Enter choice here: ")
    print(f"{player_name}'s choice is:\n{possible_choice[int(choice)]}")
    return int(choice)


def computer_choice_game():
    computer_choice = randint(0, 2)
    print(f"The computer's choice is:\n{possible_choice[computer_choice]}")
    return computer_choice


def who_win_game(A, B):  # Rock
    if A == 0:
        if B == 0:
            # print("תיקו")
            who_win_print("0")
        elif B == 1:
            # print("B ניצח")
            who_win_print("2")
        elif B == 2:
            # print("A ניצח")
            who_win_print("1")
    elif A == 1:
        if B == 0:
            # print("A ניצח")
            who_win_print("1")
        elif B == 1:
            # print("תיקו")
            who_win_print("0")
        elif B == 2:
            # print("B ניצח")
            who_win_print("2")
    elif A == 2:
        if B == 0:
            # print("B ניצח")
            who_win_print("2")
        elif B == 1:
            # print("A ניצח")
            who_win_print("1")
        elif B == 2:
            # print("תיקו")
            who_win_print("0")


def who_win_print(n):  # f6
    if n == "0":
        print("Its a Deuce!!!!!\nNo one wins!!!")
    elif n == "1":
        print(f"{name} won the game!!!!\nCongratulations!")
    elif n == "2":
        print("The computer won the game!!!!\nCongratulations!")


possible_choice = ["Rock", "Paper", "Scissors"]
welcome_game()
name = player_name_input()
play = player_choice_game(name)
pc = computer_choice_game()
who_win_game(play, pc)
# exit_menu() f7
