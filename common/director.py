import sys
import os
sys.path.append(os.pardir)

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
    def play_game(self, first_turn=1, disc_limit=64, board=None, verbose=False):
        if board is None:
            board = Board()
        assert first_turn * first_turn == 1, 'first_turn should be 1 or -1'
        turn = first_turn

        is_passed = False
        disc_count = board.get_disc_count()

        if verbose:
            board.show_status()

        while disc_count < disc_limit:
            move = self.players[turn].get_move(board, turn)
            # If there is no move for the current player
            if move == None:
                # It is not allowed to not move if it is possible to place a disc.
                # This line is for double checking, if the player is valid, we don't need this.
                # TODO: Move to tests for performance?
                if len(board.get_possible_moves(turn)) != 0:
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

            x, y = move['x'], move['y']

            # Place disc, but check it is valid
            # If not, the player algorithm has a problem.
            if not board.place_disc(x, y, turn):
                assert False, 'Player move ({y}, {x}) was invalid, quit game'.format(
                    y=y, x=x)

            # Turn goes to next player
            turn = -turn
            is_passed = False
            disc_count += 1

            if verbose:
                board.show_status()

        return board
