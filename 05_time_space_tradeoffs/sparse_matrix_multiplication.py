def sparse_matrix_multiplication(A, B):

    p = len(A)
    q = len(A[0])
    r = len(B[0])

    A_rows = [[] for _ in range(p)]
    B_rows = [[] for _ in range(q)]

    for i in range(p):
        for k in range(q):
            if A[i][k] != 0:
                A_rows[i].append((k, A[i][k]))       


    for k in range(q):
        for j in range(r):
            if B[k][j] != 0:
                B_rows[k].append((j, B[k][j]))   

    C = []

    for i in range(p):
        acumulator = {}
        for (k, v_a) in A_rows[i]:
            for (j, v_b) in B_rows[k]:
                acumulator[j] = acumulator.get(j,0) + v_a * v_b
        
        for (j, val) in acumulator.items:
            if val != 0:
                C.append((i, j, val))

    return C