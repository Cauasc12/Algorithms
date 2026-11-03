def backtrace_row_coin(C):
    if not C:
        return 0, []

    A = [0] + C
    
    n  = len(C)
    F = [0] * (n+1)
    F[1] = A[1]

    for i in range(2, n+1):
        F[i] = max(A[i] + F[i-2], F[i-1])

    coins = []
    i = n

    while i >= 1:
        if i == 1:
            coins.append(1)
            break
        if F[i] == A[i] + F[i-2]:
            coins.append(i)
            i -= 2
        else:
            i -= 1

    coins = coins[::-1]
    return F[n], coins