from common.director import Director
from player.players import *

director = Director([RandomPlayer(), RandomPlayer()])
director.play_game(verbose=True)
