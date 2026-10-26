def bigger_mobile_element(number, dir):

    n = len(number)
    k = 0
    pos_k = -1

    for i in range(n):
        pos_adj = i + dir[i]

        if pos_adj >= 0 and pos_adj < n:
            if number[i] > number[dir[i] + i] and number[i] > k:
                k = number[i]
                pos_k = i

    return k, pos_k

def johnson_trotter_permutation(input):

    """Generate permutations using adjacent swaps.
    
    Preconditions:
    Input is a nonnegative integer n (representing 1 through n), or
    a list of distinct positive numbers initially sorted increasingly.
    
    Result:
    Return all permutations as lists; consecutive permutations differ
    by one adjacent swap. An empty input returns [[]].
    """
    if isinstance(input, int):
        number = [i+1 for i in range(input)]
    else:
        number = list(input)
    
    n = len(number)
    dir = [-1] * n

    permutations = [number.copy()]

    while True:
        k, pos_k = bigger_mobile_element(number, dir)

        if pos_k == -1:
            break

        pos_adj = pos_k + dir[pos_k]
        number[pos_k], number[pos_adj] = number[pos_adj], number[pos_k]
        dir[pos_k], dir[pos_adj] = dir[pos_adj], dir[pos_k]

        for i in range(n):
            if number[i] > k:
                dir[i] = -dir[i]
        
        permutations.append(number.copy())

    return permutations