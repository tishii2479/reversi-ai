import sys
sys.path.append('..')

import unittest
from reversi.board import *


class TestBoard(unittest.TestCase):
    def test_check_placeable(self):
        board = Board()
        self.assertTrue(board.is_placeable(2, 3, 0))
        self.assertFalse(board.is_placeable(2, 3, 1))


if __name__ == "__main__":
    unittest.main()
