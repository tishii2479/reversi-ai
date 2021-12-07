from common.director import Director
from player.random_player import RandomPlayer

director = Director([RandomPlayer(), RandomPlayer()])
director.start_game()
