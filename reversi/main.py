from board import Board
import random
import time

b = Board()
turn = 1

while True:
    candidate = b.possible_place(turn)

    if len(candidate) == 0:
        turn = -turn
        if len(b.possible_place(turn)) == 0:
            break
        continue

    x, y = random.choice(candidate)
    if b.place_disc(x, y, turn):
        turn = -turn
    b.show()
    time.sleep(0.1)

print('Game end')
