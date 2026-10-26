def multi_pile_nim(piles):
    """Choose a move in normal-play Nim with multiple piles.
    
    Preconditions:
    Pile sizes are nonnegative integers. A move removes a positive
    number from exactly one pile; taking the last object wins.
    
    Result:
    Return (zero_based_pile_index, removal_count), choosing a winning
    move when possible and a legal fallback otherwise. Return None
    when no objects remain.
    """
    n = len(piles)
    min_sum = 0

    for i in range(n):
        min_sum ^= piles[i]

    if min_sum != 0:
        for i in range(n):
            if (piles[i] ^ min_sum) < piles[i]:
                remove = piles[i] - (piles[i] ^min_sum)
                return (i, remove)
    else:
        for i in range(n):
            if piles[i] > 0:
                return (i, 1)