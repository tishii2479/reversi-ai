import sys
import os
sys.path.append(os.pardir)

from reversi.board import Board
from common.director import Director
import numpy as np
import random


class Player:
    def get_move(self, board, turn):
        assert False, 'Need to implement def get_move(self, board, turn) at subclass of Player'


class RandomPlayer(Player):
    def get_move(self, board, turn):
        candidate = board.get_possible_moves(turn)

        if len(candidate) == 0:
            return None
        return random.choice(candidate)


class CNNPlayer(Player):
    def __init__(self):
        self.model = ConvolutionalNeuralNetwork()
        self.model.load_params("params.pkl")

    def get_move(self, board, turn):
        y = self.model.predict(board.get_board())
        move_idx = np.arg_max(y)
        # convert idx to (x, y)
        return {'x': move_idx % 8, 'y': move_idx / 8}


class MonteCarloPlayer(Player):
    def get_move(self, base_board, turn):
        possible_moves = base_board.get_possible_moves(turn)
        max_win_count = -1
        max_win_move = None
        board_data = base_board.get_board()

        for move in possible_moves:
            win_count = 0
            x, y = move['x'], move['y']
            test_count = 50

            for _ in range(test_count):
                board = Board(board=board_data.copy())
                board.place_disc(x, y, turn)
                director = Director([RandomPlayer(), RandomPlayer()])
                director.play_game(first_turn=-turn, board=board)
                if board.get_result() == turn:
                    win_count += 1

            if win_count > max_win_count:
                max_win_move = move

        return max_win_move
