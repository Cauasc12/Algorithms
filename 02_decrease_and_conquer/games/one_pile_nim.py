def one_pile_nim(size, max_take):
    """Choose a move in the bounded one-pile removal game.
    
    Preconditions:
    size and max_take are positive integers. A move removes between
    1 and max_take objects, without exceeding size. Taking the last wins.
    
    Result:
    Return a winning removal count when possible; otherwise return 1.
    Do not call this function after the pile is empty.
    """
    rest = size % (max_take+1)

    if rest != 0:
        return rest
    else:
        return 1