import sys
import os
sys.path.append(os.pardir)

import numpy as np
from dataset.reversi_data import *


def display_generated_data():
    (x_train, t_train), (x_test, t_test) = load_reversi_data(data_count=1000)
    open_cnt = np.zeros((8, 8))
    for i in range(len(x_train)):
        b = Board(board=x_train[i][0])
        board_data = b.get_board_copy()
        for y in range(8):
            for x in range(8):
                if board_data[y][x] == 0:
                    open_cnt[y][x] += 1

    print(open_cnt)


if __name__ == '__main__':
    display_generated_data()
