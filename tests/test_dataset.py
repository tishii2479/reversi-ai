import sys
import os
sys.path.append(os.pardir)

import unittest
from reversi.board import Board
from dataset.reversi_data import *


class TestGenerateReversiData(unittest.TestCase):
    def test_generate(self):
        x, y = generate_reversi_data(1)
        b = x[0]
        b.show_board()
        print(y)
        pass


if __name__ == '__main__':
    unittest.main()
