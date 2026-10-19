def f(n):
    print(f"my name is: {n}")


def f2():
    return "tal"


def f3():
    msg = ''
    while msg != "exit":
        msg = input("Write something:")
        print()

    while True:
        msg = input("Write something:")
        print()
        if msg == "exit":
            break


f(f2())
f3()
