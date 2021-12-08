import sys
import os
sys.path.append(os.pardir)

import unittest
from reversi.board import Board

# TODO: Add test cases


class TestBoard(unittest.TestCase):
    def test_check_placeable(self):
        b = Board()
        self.assertTrue(b.is_placeable(2, 3, 0))
        self.assertFalse(b.is_placeable(2, 3, 1))
        self.assertFalse(b.is_placeable(-1, 2, 1))
        self.assertFalse(b.is_placeable(1, 8, 1))

    def test_place_disc(self):
        b = Board()
        self.assertTrue(b.place_disc(2, 4, 1))


if __name__ == '__main__':
    unittest.main()
