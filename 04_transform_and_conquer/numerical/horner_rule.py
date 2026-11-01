def horner_rule(P, x):
    n = len(P)
    p = P[n-1]

    for i in range(n-2, -1, -1):
        p = p*x + P[i]

    return p