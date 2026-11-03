def row_coins(C):
    if not C:
        return 0, []

    n  = len(C)
    A = [0] + C

    F = [0] * (n+1)
    F[1] = a[1]

    D = [False] * (n+1)
    D[1] = True

    for i in range(2, n+1):
        if A[i] + F[i-2] >= F[i-1]:
            F[i] = A[i] + F[i-2]
            D[i] = True
        else:
            F[i] = F[i-1]
            D[i] = False

    coins = []
    i = n

    while i >= 1:
        if D[i] == True:
            coins.append(i)
            i -= 2
        else:
            i -= 1

    coins = coins[::-1]
    return F[n], coins