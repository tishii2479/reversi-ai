import sys
import os
sys.path.append(os.pardir)

import unittest
from reversi.board import Board
from dataset.reversi_data import *


class TestGenerateReversiData(unittest.TestCase):
    def test_generate(self):
        x, y = generate_reversi_data(10)
        print(x, y)
        pass


if __name__ == '__main__':
    unittest.main()
