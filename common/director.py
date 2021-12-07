import sys
sys.path.append('..')

from reversi.board import Board
import time


class Director:
    def __init__(self, players):
        assert len(players) == 2, 'Director needs two players to initialize'
        self.players = {1: players[0], -1: players[1]}

    # Play one game with self.players
    # Returns which player won:
    # 1: first, 0: draw, -1: second
    # TODO: Return board?
    def start_game(self, first_turn=1):
        board = Board()
        assert first_turn * first_turn == 1, 'first_turn should be 1 or -1'
        turn = first_turn

        is_passed = False
        while True:
            move = self.players[turn].get_move(board, turn)
            # If there is no move for the current player
            if move == None:
                # It is not allowed to not move if it is possible to place a disc.
                # This line is for double checking, if the player is valid, we don't need this.
                # TODO: Move to tests for performance?
                if len(board.get_possible_place(turn)) != 0:
                    assert False, 'Player was able to move, but did not, quit game'

                # If the previous player passed, and the current player passed,
                # it means both player can't make moves
                # Therefore, we need to end the game.
                if is_passed:
                    break

                # Pass, it will be the other player's turn
                is_passed = True
                turn = -turn
                continue

            x, y = move

            # Place disc, but check it is valid
            # If not, the player algorithm has a problem.
            if not board.place_disc(x, y, turn):
                assert False, 'Player move was invalid, quit game'

            # Turn goes to next player
            turn = -turn
            is_passed = False

        print('Game end')
        return board.show_status()
