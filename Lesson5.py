def Even_Odd():
    number = int(input("Enter a number"))

    if number % 2 == 0:
        print("Even number!")
    else:
        print("Odd number")


def triangle(n):
    for row in range(1, n + 1):
        for col in range(row):
            print("*", end="")
        print()


def exit_calc(num):
    print(f"The answer is: {num}\n Thank you, see you next time\n (:")
    exit


def calc(A, B, siman):
    answer = 0

    def plus(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a // b

    if siman == "+":
        answer = plus(A, B)
    elif siman == "/":
        answer = divide(A, B)
    elif siman == "*":
        answer = multiply(A, B)
    elif siman == "-":
        answer = minus(A, B)
    else:
        print("Error: wrong pronounce!")
        exit

    exit_calc(answer)


def entrance_calc():
    print("Welcome to Tal's calculator (:")
    print()
    msg = input("Please write an equation using:\n + or - or * or /")
    calc(int(msg[0]), int(msg[2]), msg[1])


# triangle(6)
# Even_Odd()

entrance_calc()
