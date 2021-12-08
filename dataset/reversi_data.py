import sys
import os
sys.path.append(os.pardir)

import numpy as np
import random
import pickle
from reversi.board import Board
from common.director import Director
from player.players import RandomPlayer

dataset_dir = os.path.dirname(os.path.abspath(__file__))
save_file = 'reversi_data.pkl'


def load_reversi_data(data_count=10000):
    file_path = dataset_dir + "/" + save_file

    if os.path.exists(file_path):
        print(file_path, " exists, read data.")
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            x, y = data['x'], data['y']
    else:
        print(file_path, " doesn't exist, generate data.")
        x, y = generate_reversi_data(data_count)

    data = {'x': x, 'y': y}
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

    train_count = data_count * 9 // 10
    x = np.array(x).reshape(-1, 1, 8, 8)
    y = np.array(y)
    return (x[:train_count], y[:train_count]), (x[train_count:], y[train_count:])


def generate_reversi_data(data_count):
    x, y = [], []
    remove_cnt = 5

    for i in range(data_count):
        if i % 50 == 0:
            print(i)

        director = Director([RandomPlayer(), RandomPlayer()])
        board = director.play_game(disc_limit=64 - remove_cnt)
        end_board = board.get_board()

        px, py = 0, 0

        x.append(end_board)
        t = np.zeros(64)
        t[py * 8 + px] = 1
        y.append(t)

    return x, y


if __name__ == '__main__':
    print(load_reversi_data())
