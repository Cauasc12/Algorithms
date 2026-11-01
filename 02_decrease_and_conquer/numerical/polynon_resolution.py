def polynon_resolution(P, x):
    n = len(P)
    p = P[0]
    xi = 1
    for i in range(1, n):
        xi *= x
        p = P[i]*xi +  p
    return p