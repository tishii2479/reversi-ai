import sys
sys.path.append('..')

from reversi.board import Board
import random


class RandomPlayer:
    def __init__(self):
        pass

    def get_move(self, board, turn):
        candidate = board.get_possible_place(turn)

        if len(candidate) == 0:
            return None
        return random.choice(candidate)
