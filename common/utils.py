def debug(*args):
    if False:
        print(args)


def is_valid_input(x, y):
    return (x >= 0) and (y >= 0) and (x < 8) and (y < 8)
