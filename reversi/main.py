from board import Board

b = Board()
turn = 1

while True:
    x, y = map(int, input().split())
    if b.place_disc(x, y, turn):
        turn = -turn
    b.show()
