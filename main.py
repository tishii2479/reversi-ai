from common.director import Director
from player.players import RandomPlayer

director = Director([RandomPlayer(), RandomPlayer()])
director.start_game()
