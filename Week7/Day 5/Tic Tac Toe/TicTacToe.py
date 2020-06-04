def display_board(board):
    for x in board:
        print("".join(x))


def check_input(x, y, board):
    if board[x][y] == "x" or board[x][y] == "o":
        return False
    else:
        return True


def check_win(board, p):
    if p == 1:
        c = "x"
    else:
        c = "o"
    # check vertical and horizontal lines
    for x in range(0, 3):
        if board[x][0] == c and board[x][2] == c and board[x][4] == c:
            return True
        if board[0][x*2] == c and board[1][x*2] == c and board[2][x*2] == c:
            return True

    # check cross lines
    if board[0][0] == c and board[1][2] == c and board[2][4] == c:
        return True
    if board[0][4] == c and board[1][2] == c and board[2][0] == c:
        return True

    return False


def play():
    player = 1

    board = [["_", "|", "_", "|", "_"], ["_", "|", "_", "|", "_"], [" ", "|", " ", "|", " "]]

    while True:

        display_board(board)
        print("player {}, please enter coordinates for your turn (x,y)".format(player))
        x, y = input(">>").split(",")
        x = int(x)
        y = int(y)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("wrong input, please try again")
            continue;
        x = x - 1
        y = (y -1)*2
        if not check_input(x, y, board):
            print("wrong inputs, please try again")
            continue;
        if player == 1:
            board[x][y] = "x"
        else:
            board[x][y] = "o"

        if check_win(board, player) == True:
            display_board(board)
            print("Player {} Wins!".format(player))

            return
        if player == 1:
            player = 2
        else:
            player = 1


if __name__ == "__main__":
    play()
