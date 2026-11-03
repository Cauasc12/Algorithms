def shift_table(P):
    m = len(P)
    table = {}

    for i in range(m-1):
        table[P[i]] = m-1-i

    return table

def horspool_matching(P, T):
    m = len(P)
    n = len(T)
    if m == 0:
        return 0
    if m > n:
        return -1

    table = shift_table(P)
    i = m-1

    while i <= n-1:
        k = 0
        while k < m and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            i += table.get(T[i], m)

    return -1