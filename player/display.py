import sys
import os
sys.path.append(os.pardir)

import numpy as np
from player.players import *
from dataset.reversi_data import *


def play_cnn_player():
    player = CNNPlayer()
    (x_train, t_train), (x_test, t_test) = load_reversi_data(data_count=1000)
    placeable_count = 0
    move_cnt = np.zeros((8, 8))
    possible_cnt = np.zeros((8, 8))

    for i in range(1000):
        b = Board(board=x_test[i][0])
        # b.show_board()
        turn = 1
        move = player.get_move(b, turn)
        print('best move is', move)
        y = np.zeros(64)
        t_idx = np.argmax(t_test[i])
        placeable_count += b.is_placeable(move['x'], move['y'], turn)
        move_cnt[move['y']][move['x']] += 1

        for i in range(8):
            for j in range(8):
                if b.is_placeable(j, i, turn):
                    possible_cnt[i][j] += 1

    print(placeable_count / 1000)
    print(move_cnt)
    print(possible_cnt)


def play_monte_carlo_player():
    player = MonteCarloPlayer()
    x, t = generate_reversi_data(10)
    for i in range(10):
        b = Board(board=x[i])
        # b.show_board()
        turn = 1
        move = player.get_move(b, turn)
        print('best move is', move)
        y = np.zeros(64)
        t_idx = np.argmax(t[i])
        tx, ty = t_idx % 8, t_idx // 8
        assert move['x'] == tx and move['y'] == ty, 'move: {move}, t_idx: {t_idx}'.format(
            move=move, t_idx=t_idx)


if __name__ == '__main__':
    play_cnn_player()
