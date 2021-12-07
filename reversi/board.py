import sys
import numpy as np
sys.path.append('..')

from common.utils import is_valid_input


class Board:
    def __init__(self):
        self._board = [[0] * 8 for i in range(8)]
        self._board[3][3] = self._board[4][4] = 1
        self._board[4][3] = self._board[3][4] = -1

    def place_disc(self, x, y, turn):
        if not is_valid_input(x, y):
            print(
                'Invalid placement: disc can not be set at ({y}, {x})'.format(y=y, x=x))
            return False
        if self._board[y][x] != 0:
            print(
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
            print(
                'Invalid placement: disc is not placeable at ({y}, {x})'.format(y=y, x=x))
            return False

        self._board[y][x] = turn
        return True

    def show(self):
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
