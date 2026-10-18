def is_even(num):
    return num % 2 == 0


def all_square(n):
    for row in range(n):
        for col in range(n):
            print("+", end="")
        print()


def Shora():
    print()
    print("---------------------------------------- + ----------------------------------------")
    print("---------------------------------------- + ----------------------------------------")
    print()


def Triangle_nums(n):
    for i in range(1, n + 1):
        print(str(i) * i)


def Triangle_letters(letters):
    for row in range(len(letters)):
        for col in range(row + 1):
            print(letters[row], end="")
        print()


def Loop_count_stars(size):
    for row in range(size):
        for col in range(row + 1):
            print("*", end="")
        print()


def Stars_n_space(n):
    for row in range(n):
        for col in range(n - (row + 1)):
            print(".", end="")

        for col in range(row + 1):
            print("*", end="")
        print()


def half_n_half(n):
    for row in range(n):
        for col in range(n):
            if col > n / 2:
                print(".", end="")
            else:
                print("*", end="")
        print()


def Yahalom(n):
    size = n * 2
    flag = 1
    for row in range(size // 2):
        for col in range(1, size // 2 - row):
            print(" ", end="")
        print("*" * flag, end="")
        for col in range(1, size // 2 - row):
            print(" ", end="")
        flag += 2
        print()
    flag -= 4
    for row in range(1, size // 2):
        for col in range(1, row + 1):
            print(" ", end="")
        print("*" * flag, end="")
        for col in range(1, row + 1):
            print(" ", end="")
        flag -= 2

        print()


def XOXO(n):
    for row in range(n):
        for col in range(n + 1):
            if is_even(col):
                print("X", end="")
            else:
                print("O", end="")
        print()


def Dogma(size):
    for row in range(size):
        for col in range(size):
            if col == (size - 1):
                print("*", end="")
            else:
                print("-", end="")
        print()


Shora()
all_square(10)
Shora()
Triangle_nums(9)
Shora()
Triangle_letters("ABCDEFG")
Shora()
Loop_count_stars(9)
Shora()
Stars_n_space(9)
Shora()
half_n_half(5)
Shora()
Yahalom(5)
Shora()
XOXO(5)
Shora()

Dogma(4)
