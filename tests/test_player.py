import sys
import os
sys.path.append(os.pardir)

import numpy as np
import unittest
from player.players import *
from dataset.reversi_data import *


class TestCNNPlayer(unittest.TestCase):
    def test_get_move(self):
        player = CNNPlayer()
        x, t = generate_reversi_data(data_count=10)
        cnt = 0
        for i in range(10):
            b = Board(board=x[i])
            # b.show_board()
            turn = 1
            move = player.get_move(b, turn)
            print('best move is', move)
            y = np.zeros(64)
            t_idx = np.argmax(t[i])
            cnt += b.is_placeable(move['x'], move['y'], turn)
        print(cnt / 100)


class TestDeepCNNPlayer(unittest.TestCase):
    def test_get_move(self):
        player = DeepCNNPlayer()
        x, t = generate_reversi_data(data_count=10)
        cnt = 0
        for i in range(10):
            b = Board(board=x[i])
            b.show_board()
            turn = 1
            move = player.get_move(b, turn)
            print('best move is', move)
            y = np.zeros(64)
            t_idx = np.argmax(t[i])
            cnt += b.is_placeable(move['x'], move['y'], turn)
        print(cnt / 100)


class TestMonteCarloPlayer(unittest.TestCase):
    def test_get_move(self):
        player = MonteCarloPlayer()
        x, t = generate_reversi_data(10)
        for i in range(10):
            b = x[i]
            b.show_board()
            turn = 1
            move = player.get_move(b, turn)
            print('best move is', move)
            y = np.zeros(64)
            t_idx = np.argmax(t[i])
            self.assertTrue(move['x'] == t_idx %
                            8 and move['y'] == t_idx // 8, 'move: {move}, t_idx: {t_idx}'.format(move=move, t_idx=t_idx))


if __name__ == '__main__':
    unittest.main()
