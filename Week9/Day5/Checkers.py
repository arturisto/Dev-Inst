class GamePiece:

    def __init__(self, player):
        self.icon = None
        self.player = player


class Pawn(GamePiece):

    def __init__(self, player):
        super().__init__(player)
        if self.player == 0:
            self.icon = u"\u265F"
        else:
            self.icon = u"\u2659"


class Queen(GamePiece):

    def __init__(self, player):
        super().__init__(player)
        if self.player == 0:
            self.icon = u'\u2655'
        else:
            self.icon = u'\u265B'


class gameBoard:
    possible_move_multipliers = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

    def __init__(self):
        self.board = [[Pawn(0), u'\u25FB'] * 4,
                      [u"\u25FB", Pawn(0)] * 4,
                      [Pawn(0), u'\u25FB'] * 4,
                      [u'\u25FB', u'\u25FC'] * 4,
                      [u"\u25FC", u'\u25FB'] * 4,
                      [u'\u25FB', Pawn(1)] * 4,
                      [Pawn(1), u'\u25FB'] * 4,
                      [u'\u25FB', Pawn(1)] * 4
                      ]
        self.clean_board = [[(u"\u25FC"), (u'\u25FB')] * 4,
                            [(u"\u25FB"), (u'\u25FC')] * 4,
                            [(u"\u25FC"), (u'\u25FB')] * 4,
                            [(u"\u25FB"), (u'\u25FC')] * 4,
                            [(u"\u25FC"), (u'\u25FB')] * 4,
                            [(u"\u25FB"), (u'\u25FC')] * 4,
                            [(u'\u25FC'), (u'\u25FB')] * 4,
                            [(u"\u25FB"), (u'\u25FC')] * 4
                            ]
        self.score = [12, 12]

    def print_board(self):
        line = ""
        for x in range(0, 8):
            line += " " + str(x) + " "
        print(line)
        for i, board_line in enumerate(self.board):
            line = str(i)
            for item in board_line:
                if isinstance(item, GamePiece):
                    line += " " + item.icon
                else:
                    line += " " + item
            print(line)

    def move_item(self, player, origin, target):

        # check if origin is empty cell
        # target is a game piece,
        # player moves not his piece

        # if so, give error:
        if (isinstance(self.board[origin[0]][origin[1]], GamePiece)) != True or isinstance(
                self.board[target[0]][target[1]], GamePiece) or self.board[origin[0]][origin[1]].player != player:
            print("not a valid move")
            return 0
        if origin[0] == target[0] or origin[1] == target[1]:
            print("not a valid move")
            return 0
        # check if item is queen
        if isinstance(self.board[origin[0]][origin[1]], Queen):

            # check validity of movement of queen

            if origin[0] < target[0] and origin[1] < target[1]:  # move down and right
                multiplier = 0
            elif origin[0] > target[0] and origin[1] < target[1]:  # move up and right
                multiplier = 1
            elif origin[0] < target[0] and origin[1] > target[1]:  # move down and left
                multiplier = 3
            else:  # move down and left
                multiplier = 2
            previous_game_piece = False
            eaten_pieces = 0
            # check if queen's move is valid, including eating:
            for i in range(1, abs(target[0] - origin[0])):

                if isinstance(self.board[origin[0] + self.possible_move_multipliers[multiplier][0] * i][
                                  origin[1] + self.possible_move_multipliers[multiplier][1] * i],
                              GamePiece):
                    # check if there are two consequitive game pieces
                    if previous_game_piece or self.board[origin[0] + self.possible_move_multipliers[multiplier][0] * i][
                        origin[1] + self.possible_move_multipliers[multiplier][1] * i].player == player:
                        print("not a valid move")
                        return 0
                    else:
                        previous_game_piece = True
                        eaten_pieces += 1
                else:
                    previous_game_piece = False

            # move queen
            self.perform_move(origin, target, player)
            for i in range(abs(target[0] - origin[0]) - 1):
                self.board[origin[0] + self.possible_move_multipliers[multiplier][0] * i][
                    origin[1] + self.possible_move_multipliers[multiplier][1] * i] = \
                    self.clean_board[origin[0] + self.possible_move_multipliers[multiplier][0] * i][
                        origin[1] + self.possible_move_multipliers[multiplier][1] * i]
            self.check_win(player, eaten_pieces)

            return 1
        else:  # not queen

            # check validity of move

            if abs(target[0] - origin[0]) == 1:  # regular move, not eat
                if (player == 0 and origin[0] > target[0]) or (player == 1 and origin[0] < target[0]):
                    # player 0 always moves down, player 1 always moves up the grid
                    print("not a valid move")
                    return 0
                else:  # valid move
                    self.perform_move(origin, target, player)
                    return 1
            else:  # eat move
                # eat
                output = self.eat_move(origin, target, player)
                if output == 2:
                    return 2
                elif output == 0:
                    return 0
                else:
                    return 1

    def perform_move(self, origin, target, player):
        self.board[target[0]][target[1]], self.board[origin[0]][origin[1]], = self.board[
                                                                                  origin[0]][origin[1]], \
                                                                              self.board[
                                                                                  target[0]][target[1]]
        # check if move made it to the end of board, if so make the piece a queen
        if (target[0] == 7 and player == 0) or (target[0] == 0 and player == 1):
            self.board[target[0]][target[1]] = Queen(player)

    def eat_move(self, origin, target, player):

        coord_eat = (int((origin[0] + target[0]) / 2), int((origin[1] + target[1]) / 2))

        # check if the "eaten" object is in fact a game piece
        if isinstance(self.board[coord_eat[0]][coord_eat[1]], Pawn) or isinstance(
                self.board[coord_eat[0]][coord_eat[1]], Queen):
            # put an empty tile into the "eaten" cell
            if self.board[coord_eat[0]][coord_eat[1]].player == player:
                print("not a valid move")
                return 0
            self.board[coord_eat[0]][coord_eat[1]] = self.clean_board[coord_eat[0]][coord_eat[1]]
            self.perform_move(origin, target, player)

            output = self.check_win(player, 1)

            if output == 2:
                return 2
        else:
            print("not a valid move")
            return 0

        return 1

    def check_win(self, player, score):
        self.score[player - 1] -= score
        if self.score[player - 1] <= 0:
            print(f"player {player} wins!")
            return 2
        return 1


def check_input(user_input):
    try:
        input_to_check = user_input.split(",")
        if 0 <= int(input_to_check[0]) <= 7 and 0 <= int(input_to_check[1]) <= 7:
            return False
        else:
            return True
    except:
        return True


def main():
    # print specific rules:
    print(""" This game has the following difference from the original game:
       1. a pawn can eat only 1 other pawn in any direction, regardless the possibility of eating another one
       2. queen can eat any number of pawn on a single line as long there is at least one empty cell between each pawn       
       """)
    board = gameBoard()
    board.print_board()
    curr_player = 0


    print(f"Player {curr_player + 1} turn")

    while True:

        origin_input = input("enter coordinates of piece to move (x,y): ")
        if check_input(origin_input):
            print("wrong input")
            continue
        origin_input = origin_input.split(",")
        target_input = input("enter coordinates of target (x,y): ")
        if check_input(target_input):
            print("wrong input")
            continue
        target_input = target_input.split(",")
        origin_input = (int(origin_input[0]), int(origin_input[1]))
        target_input = (int(target_input[0]), int(target_input[1]))

        output = board.move_item(curr_player, origin_input, target_input)
        if output == 1:
            curr_player = (curr_player + 1) % 2
            board.print_board()
            print(f"Player {curr_player + 1} turn")
        elif output == 2:
            return


if __name__ == "__main__":
    main()
