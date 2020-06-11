import random
import copy


class Cell:

    def __init__(self, position):
        self.is_alive = position


class Grid:
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, n, grid=None):
        if grid is None:
            self.game = [[Cell() for _ in range(n)] for _ in range(n)]
        else:
            self.game = [[0] * n for _ in range(n)]
            for i, x in enumerate(grid):
                for j, y in enumerate(x):
                    self.game[i][j] = Cell(y)
        self.size = n
        self.next_gen = copy.deepcopy(self.game)

    def play_life(self):
        while True:
            x = 1
            for i in range(self.size):
                for j in range(self.size):
                    self.next_gen[i][j] = self.check_next_gen(self.game[i][j], i, j)

            self.game = copy.deepcopy(self.next_gen)
            self.print_grid()

    def check_next_gen(self, current_cell, i, j):

        live_neighbours = 0
        dead_neighbours = 0

        for x in self.neighbours:  # for each position around the cell
            # check if the neighbour is inside the game board
            if 0 <= i + x[0] < self.size and 0 <= j + x[1] < self.size:
                if self.game[i + x[0]][j + x[1]].is_alive == 1:
                    live_neighbours += 1
                else:
                    dead_neighbours += 1
        if current_cell.is_alive == 0:  # is the cell is dead
            if live_neighbours == 3:
                return Cell(1)
            else:
                return Cell(0)
        else:
            if 2 <= live_neighbours <= 3:
                return Cell(1)
            else:
                return Cell(0)

    def print_grid(self):

        for x in self.game:
            print_list = []
            for y in x:
                print_list.append(y.is_alive)
            print(print_list)

        print("*" * 32)


def main():

    grid = Grid(6, [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0]])
    grid.print_grid()
    grid.play_life()


if __name__ == "__main__":
    main()
