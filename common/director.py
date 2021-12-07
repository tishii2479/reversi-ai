import sys
sys.path.append('..')

from reversi.board import Board
import time


class Director:
    def __init__(self, players):
        assert len(players) == 2, "Director needs two players to initialize"
        self.players = {1: players[0], -1: players[1]}

    def start_game(self):
        board = Board()
        turn = 1

        is_passed = False
        while True:
            move = self.players[turn].get_move(board, turn)
            if move == None:
                if is_passed:
                    break
                is_passed = True
                turn = -turn
                continue

            x, y = move
            if not board.place_disc(x, y, turn):
                print("Player move was invalid, quit game")
                exit(1)
            turn = -turn
            is_passed = False
            board.show_board()
            time.sleep(0.1)

        print('Game end')
        board.show_result()
