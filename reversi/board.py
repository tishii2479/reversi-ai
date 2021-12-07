import sys
sys.path.append('..')

import numpy as np
from common.utils import *


class Board:
    def __init__(self):
        self._board = [[0] * 8 for i in range(8)]
        self._board[3][3] = self._board[4][4] = 1
        self._board[4][3] = self._board[3][4] = -1

    def place_disc(self, x, y, turn, do_flip=True):
        if not is_valid_input(x, y):
            debug(
                'Invalid placement: disc can not be set at ({y}, {x})'.format(y=y, x=x))
            return False
        if self._board[y][x] != 0:
            debug(
                'Invalid placement: disc already exist at ({y}, {x})'.format(y=y, x=x))
            return False

        # Check 8 directions if there is a disc that will be flipped
        directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                      (0, -1), (-1, -1), (-1, 0), (-1, 0)]

        has_flipped = False
        for dx, dy in directions:
            has_other_stone = False
            for i in range(1, 8):
                px, py = x + dx * i, y + dy * i
                if not is_valid_input(px, py):
                    break
                v = self._board[py][px]

                if (v == turn) and has_other_stone:
                    if do_flip:
                        # flip all
                        for j in range(1, i + 1):
                            self._board[y + dy * j][x + dx * j] = turn
                    has_flipped = True
                    break
                if v == -turn:
                    has_other_stone = True
                    continue
                else:
                    break

        if not has_flipped:
            debug(
                'Invalid placement: disc is not placeable at ({y}, {x})'.format(y=y, x=x))
            return False

        if do_flip:
            self._board[y][x] = turn
        return True

    def is_placeable(self, x, y, turn):
        return self.place_disc(x, y, turn, False)

    def show_board(self):
        for i in range(8):
            for j in range(8):
                v = self._board[i][j]
                if v == 0:
                    print('.', end='')
                elif v == 1:
                    print('●', end='')
                elif v == -1:
                    print('◯', end='')
                else:
                    assert False
            print()
        print()

    def get_possible_place(self, turn):
        candidate = []
        for i in range(8):
            for j in range(8):
                if self.is_placeable(i, j, turn):
                    candidate.append((i, j))
        return candidate

    def show_result(self):
        self.show_board()
        first, second = 0, 0
        for i in range(8):
            for j in range(8):
                if self._board[i][j] == 1:
                    first += 1
                elif self._board[i][j] == -1:
                    second += 1

        print("First: {first}, Second: {second}".format(
            first=first, second=second))

        if first > second:
            return 1
        elif first == second:
            return 0
        else:
            return -1
