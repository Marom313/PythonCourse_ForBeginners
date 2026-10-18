def Abbale(Val):
    if Val == 5:
        print("55555555555555555555")
    elif Val == 4:
        print("44444444444444444444")
    elif Val == 3:
        print("33333333333333333333")
    elif Val == 2:
        print("22222222222222222222")
    elif Val == 1:
        print("11111111111111111111")
    elif Val == 0:
        print("00000000000000000000")
    else:
        print("הערך שנקלט, לא בין 0-5")


def is_even(num):  # True if even False if odd
    return num % 2 == 0


def Testkatan():
    size = 10
    for i in range(size):
        if not is_even(i):
            print(str(i) * i)
        else:
            print("Odd Number" + " " + str(i) * i)


# Abbale("Kaka")


Testkatan()
#
# for i in range(size):
#     if is_even(i):
#         print("Even Number" + " " + str(i) * i)
#     else:
#         print(str(i) * i)
