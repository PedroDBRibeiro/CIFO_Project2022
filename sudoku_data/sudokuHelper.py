import numpy

def get_box_indices(base=3):
    # total length of outer box
    side = base * base
    # init with list of Nones
    box_idx = [None for _ in range(side)]
    # flat index of length i*j
    pos = 0
    for i in range(base):
        for j in range(base):
            # define starting value for each box
            start = i * base * side + j * base
            # c: starting point of each row inside box
            # r: add rows inside box
            box_idx[pos] = [start + c * side + r for c in range(base) for r in range(base)]
            pos += 1

    return box_idx


def get_col_indices(base):
    side = base * base
    return [numpy.arange(i, side * side, side).tolist() for i in list(range(side))]


def get_row_indices(base):
    side = base * base
    return [list(range(i, i + side)) for i in numpy.arange(0, side * side, side)]


def get_indices(base):
    row_idx = get_row_indices(base)
    col_idx = get_col_indices(base)
    box_idx = get_box_indices(base)
    return row_idx, col_idx, box_idx


def count_duplicates(seq):
    """
    based on https://stackoverflow.com/questions/52090212/counting-the-number-of-duplicates-in-a-list/52090695
    takes as argument a sequence and
    returns the number of duplicate elements
    :param seq: list of numbers
    :return: int of duplicate numbers inside list
    """
    counter = 0
    seen = set()
    for elm in seq:
        if elm in seen:
            counter += 1
        else:
            seen.add(elm)
    return counter
