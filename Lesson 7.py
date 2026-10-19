# # Example:
# # if (statement):
# #    (True)
# #                (False)
# import random
# from random import randint
#
#
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def bigger(a, b):
#     if (a > b):
#         return a
#     elif (a < b):
#         return b
#     else:
#         return 0
#
#
# def grill():
#     number = random.randint(1, 10)
#     for i in range(number, 0, -1):
#         print(i)
#
#
# grill()


# -----------------------------------------------------  Tic Tac Toe  ------------------------------------------------------------------------------------------
"""
פה תרשום הערות ודברים שאתה רוצה לסגור תוך כדי כתיבת הקוד.

"""


def play_game():
    def welcome():
        print("welcome to tic tac toe")

    def create_board():
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board(board):
        print()
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--|---|--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--|---|--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        print("--|---|--")
        print()

    def player_move(board, player):
        pass

    welcome()
    board = create_board()
    print_board(board)
    player = "X"
    player_move(board, player)
    check_winner(board, player)
    is_board_full(board)  # Return True\False
    switch_player(player)
    bye_bye_print(player)


play_game()
