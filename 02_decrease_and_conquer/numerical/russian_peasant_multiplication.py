def russian_peasant_multiplication(n, m):
    """Multiply integers through halving, doubling, and addition.
    
    Preconditions:
    n must be a nonnegative integer; m may be any integer.
    
    Result:
    Return n * m.
    """
    if n == 0 or m == 0:
        return 0

    if n % 2 == 0:
        return russian_peasant_multiplication(n>>1, m<<1)
    else:
        return russian_peasant_multiplication(n>>1, m<<1) + m