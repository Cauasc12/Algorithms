def right_cyclic_shift_space(S, T):
    n = len(S)
    m = len(T)

    if n != m:
        return False

    for i in range(n):
        match = True
        for j in range(m):
            if T[j] != S[(j+i) % n]:
                match = False
                break
        if match:
            return True

    return False