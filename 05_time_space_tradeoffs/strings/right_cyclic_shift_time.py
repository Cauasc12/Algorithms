def bad_symble_shift(P):
    m = len(P)
    table = {}

    for i in range(m):
        table[P[i]] = i

    return table

def good_suffix_shift(P):
    m = len(P)
    table = [0] * (m+1)
    border = [0] * (m+1)

    i = m
    j = m+1
    border[i] = j

    while i > 0:
        while j <= m and P[i-1] != P[j-1]:
            if table[j] == 0:
                table[j] = j-i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    j = border[0]
    for i in range(m+1):
        if table[i] == 0:
            table[i] = j
        if i == j:
            j = border[j]

    return table

def boyer_moore(P, T):
    m = len(P)
    n = len(T)

    if m == 0:
        return 0
    if m > n:
        return -1

    bs_table = bad_symble_shift(P)
    gs_table = good_suffix_shift(P)

    i = m-1
    while i <= n-1:
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            last = bs_table.get(T[i-k], -1)
            mismatch_position = m - 1 - k
            bs_shift = mismatch_position - last
            d1 = max(bs_shift, 1)
            if k == 0:
                i += d1
            elif k > 0:
                d2 = gs_table[m-k]
                i += max(d1, d2)

    return -1

def right_cyclic_shift_time(S, T):
    n = len(S)
    m = len(T)

    if n != m:
        return False   

    CS = S + S

    if boyer_moore(T, CS) != -1:
        return True
    return False