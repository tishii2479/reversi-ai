import sys
import os
sys.path.append(os.pardir)

from reversi.board import Board
from common.director import Director
from model.function import *
import numpy as np
from model.cnn import ConvolutionalNeuralNetwork
import random


class Player:
    # Base class for player
    # Each Player should override def get_move(self, board, turn):
    # board: reversi.board.Board
    # turn: which get which turn is the player
    def get_move(self, board, turn):
        assert False, 'Need to implement def get_move(self, board, turn) at subclass of Player'


class RandomPlayer(Player):
    # Player who selects move randomly
    def get_move(self, board, turn):
        candidate = board.get_possible_moves(turn)

        if len(candidate) == 0:
            return None
        return random.choice(candidate)


class CNNPlayer(Player):
    # Player that uses convolutional network
    def __init__(self):
        self.network = ConvolutionalNeuralNetwork()
        self.network.load_params("params.pkl")

    def get_move(self, board, turn):
        y = self.network.predict(board.get_board_copy().reshape(-1, 1, 8, 8))
        y = softmax(y[0])
        move_idx = np.argmax(y)
        # convert idx to (x, y)
        return {'x': move_idx % 8, 'y': move_idx // 8}


class MonteCarloPlayer(Player):
    # Player that uses monte carlo to get move
    # It is mainly used to generate reversi board data
    # TODO: Use better algorithm
    def get_move(self, base_board, turn):
        possible_moves = base_board.get_possible_moves(turn)
        max_win_count = -1
        max_win_move = None
        board_data = base_board.get_board_copy()

        for move in possible_moves:
            win_count = 0
            x, y = move['x'], move['y']
            test_count = 10

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
