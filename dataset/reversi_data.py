import sys
import os
sys.path.append(os.pardir)

import numpy as np
import random
import pickle
from reversi.board import Board
from common.director import Director
from player.players import RandomPlayer, MonteCarloPlayer

dataset_dir = os.path.dirname(os.path.abspath(__file__))
save_file = 'reversi_data.pkl'


def load_reversi_data(data_count=10000):
    # Returns reversi dataset at file_path
    # If dataset does not exist, generate by using generate_reversi_data(data_count)

    file_path = dataset_dir + "/" + save_file

    if os.path.exists(file_path):
        print(file_path, "exists, read data.")
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            x, y = data['x'], data['y']
    else:
        print(file_path, "doesn't exist, generate data.")
        x, y = generate_reversi_data(data_count)
        data = {'x': x, 'y': y}
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        print('generated data to', file_path)

    x = np.array(x).reshape(-1, 1, 8, 8)
    y = np.array(y)
    train_count = data_count * 9 // 10
    nx = []
    for e in x:
        for i in range(4):
            nx.append(np.rot90(e, i, axes=(1, 2)))
    x = np.array(nx)
    np.random.shuffle(x)
    np.random.shuffle(y)
    x = x[:data_count]
    y = y[:data_count]
    return (x[:train_count], y[:train_count]), (x[train_count:], y[train_count:])


def generate_reversi_data(data_count):
    # Generate reversi dataset
    # TODO: Improve algorithm

    x, y = [], []
    remove_cnt = 6
    mcPlayer = MonteCarloPlayer()

    for i in range(data_count):
        if i != 0 and i % 50 == 0:
            print(i)

        move = None

        while move == None:
            director = Director([RandomPlayer(), RandomPlayer()])
            board = director.play_game(disc_limit=64 - remove_cnt)
            move = mcPlayer.get_move(board, 1)

        tx, ty = move['x'], move['y']

        x.append(board.get_board_copy())
        tv = np.zeros(64)
        tv[ty * 8 + tx] = 1
        y.append(tv)
    return x, y


if __name__ == '__main__':
    print(load_reversi_data())
