# def f(n):
#     print(f"my name is: {n}")
# #
# #
# def f2():
#     return "tal"
# #
# #
# def f3():
#     msg = ''
#     while msg != "exit":
#         msg = input("Write something:")
#         print()
#
#     while True:
#         msg = input("Write something:")
#         print()
#         if msg == "exit":
#             break
# #
#
#
#
# f(f2())
# f3()


def my_type(T):
    return type(T)


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
        while True:
            choice = input(f"Player {player},choose 1-9:")
            if not choice.isdigit():
                print("Please enter a number!!!")
                continue
            position = int(choice)
            if position < 1 or position > 9:
                print("Choose a number between 1-9")
                continue
            index = position - 1
            if board[index] == "X" or board[index] == "O":
                print("This position is already taken! ")
                continue
            board[index] = player
            break

    def check_winner(board, player):
        if board[0] == player and board[1] == player and board[2] == player:
            return True
        elif board[3] == player and board[4] == player and board[5] == player:
            return True
        elif board[6] == player and board[7] == player and board[8] == player:
            return True
        elif board[0] == player and board[3] == player and board[6] == player:
            return True
        elif board[1] == player and board[4] == player and board[7] == player:
            return True
        elif board[2] == player and board[5] == player and board[8] == player:
            return True
        elif board[0] == player and board[4] == player and board[8] == player:
            return True
        elif board[2] == player and board[4] == player and board[6] == player:
            return True
        else:
            return False

    def is_board_full(board):
        for i in board:
            if i != "X" and i != "O":
                return False
        return True

    def switch_player(player):
        if player == "X":
            return "O"
        else:
            return "X"

    # welcome()
    # board = create_board()
    # print_board(board)
    # player = "X"
    # player_move(board, player)
    # check_winner(board, player)
    # is_board_full(board)  # Return True\False
    # switch_player(player)

    welcome()

    board = create_board()
    player = "X"

    while True:

        print_board(board)

        player_move(board, player)

        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} WINS!")
            break

        if is_board_full(board):
            print_board(board)
            print("🤝 It's a DRAW!")
            break

        player = switch_player(player)


# Start the game
play_game()
