import sys
import unittest

sys.path.append('..')

from reversi.board import *


class TestBoard(unittest.TestCase):
    def test_check_placeable(self):
        board = Board()
        self.assertTrue(board.place_disc(2, 3, 0))
        board = Board()
        self.assertFalse(board.place_disc(2, 3, 1))


if __name__ == "__main__":
    unittest.main()
