def Game():
    flag = True
    print("Welcome to the Guess Game! ")
    num = int(input("Pick a number from 0 to 100"))
    guess = int(input("now, guess the number: "))
    while flag:
        if guess == num:
            print("Nice One!! YOU MADE IT !")
            print(str(num) + " is the number yo have entered.")
            pick = int(input("Enter 1 if you want to play again,\nEnter 0 is you want to exit (:"))
            if pick == 0:
                print("Thank you very much (:")
                flag = False
        elif guess < num:
            print('Your guess is lower then num ):')
            guess = int(input("Try again: "))
        elif guess > num:
            print('Your guess is higher then num ):')
            guess = int(input("Try again: "))


def start_game():
    Game()


start_game()
