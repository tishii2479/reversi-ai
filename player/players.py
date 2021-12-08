import sys
import os
sys.path.append(os.pardir)

from reversi.board import Board
import numpy as np
import random


class Player:
    def get_move(self, board, turn):
        assert False, 'Need to implement def get_move(self, board, turn) at subclass of Player'


class RandomPlayer(Player):
    def get_move(self, board, turn):
        candidate = board.get_possible_place(turn)

        if len(candidate) == 0:
            return None
        return random.choice(candidate)


class CNNPlayer(Player):
    def __init__(self):
        self.model = ConvolutionalNeuralNetwork()
        self.model.load_params("params.pkl")

    def get_move(self, board, turn):
        y = self.model.predict(board)
        print(board, y)
        move = np.arg_max(y)
        return move
