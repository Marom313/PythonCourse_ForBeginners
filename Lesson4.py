import random


def Shoora():
    print("---------------------------------------------------------------------------------")
    print()


def g(guess, n):
    if guess < n:
        msg = "Too Low"
    elif guess > n:
        msg = "Too High"
    else:
        msg = "Right Answer! you got the right number. "

    return msg


def main_game():
    Shoora()
    print("Hello welcome to the GUESSING GAME!")
    print()
    print("The program will pick a number from 0 to 100: ")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("💡 The program had picked the number, lts go!  ")
    print()
    num = random.randint(0, 99)
    user_guess = int(input("Please guess a number between 0 to 100: "))
    if user_guess >= 100 or user_guess < 0:
        print("Bad guess, it has to be between 0 to 100 not included.")
        return
    print(user_guess)

    while g(user_guess, num) != "Right Answer! you got the right number. ":
        print(g(user_guess, num))
        user_guess = int(input("Please guess a number between 0 to 100: "))
        if user_guess >= 100 or user_guess < 0:
            print("Bad guess, it has to be between 0 to 100 not included.")
            return
        print(user_guess)

    print("You got the right answer!! its: ", num)


main_game()
