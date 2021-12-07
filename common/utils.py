def debug(*args):
    # TODO: add options to switch this flag
    if False:
        print(args)


def is_valid_place(x, y):
    return (x >= 0) and (y >= 0) and (x < 8) and (y < 8)
