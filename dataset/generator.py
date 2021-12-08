import sys
import os
sys.path.append('..')

import numpy as np
import random
import pickle
from reversi.board import Board
from common.director import Director
from player.players import RandomPlayer


save_file = 'reversi_data.pkl'


def load_reversi_data():
    data_count = 10000

    if os.path.exists(save_file):
        with open(save_file, 'rb') as f:
            data = pickle.load(f)
            x, y = data['x'], data['y']
    else:
        x, y = [], []

        for i in range(data_count):
            if i % 50 == 0:
                print(i)

            director = Director([RandomPlayer(), RandomPlayer()])
            board = director.play_game()
            end_board = board.get_np_board()

            px, py = 0, 0
            while (px < 2 or 5 < px) or (py < 2 or 5 < py) or (end_board[py][px] == 0):
                px = random.randrange(0, 8)
                py = random.randrange(0, 8)

            x.append(end_board)
            t = np.zeros(64)
            t[py * 8 + px] = 1
            y.append(t)

        data = {'x': x, 'y': y}
        with open(save_file, 'wb') as f:
            pickle.dump(data, f)

    train_count = data_count * 9 // 10
    x = np.array(x).reshape(-1, 1, 8, 8)
    y = np.array(y)
    return (x[:train_count], y[:train_count]), (x[train_count:], y[train_count:])


if __name__ == '__main__':
    print(load_reversi_data())
