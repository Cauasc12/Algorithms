def telephone_biils(t, b):
    n = len(t)
    m = len(b)

    t = sorted(t)
    b = sorted(b)

    i = 0
    j = 0

    unpaid = []

    while i < n and j < m:
        if t[i] == b[j]:
            i += 1
            j += 1
        elif t[i] < b[j]:
            unpaid.append(t[i])
            i += 1
        else:
            j += 1

    while j < m:
        unpaid.append(t[i])
        j += 1

    return unpaid