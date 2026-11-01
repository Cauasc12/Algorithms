def gaussian_elimination(A, B):
    augmented = forward_elimination(A, B)
    if not augmented:
        return [] 
    return back_substitution(augmented)

def forward_elimination(A, B):
    n = len(A) 
    for i in range(n):
        A[i].append(B[i])

    for i in range(n-1):
        pivot_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[pivot_row][i]):
                pivot_row = j

        A[i], A[pivot_row] = A[pivot_row], A[i]

        if A[i][i] == 0:
            return []

        for j in range(i+1, n):
            temp = A[j][i] / A[i][i]
            for k in range(i,n+1):
                A[j][k] -= A[i][k] * temp

    return A

def back_substitution(A):
    n = len(A)
    x = [0.0] * n

    for i in range(n-1, -1, -1):
        if A[i][i] == 0:
            return []

        agregate = 0.0
        for j in range(i+1, n):
            agregate += A[i][j] * x[j]

        x[i] = (A[i][n] - agregate) / A[i][i]

    return x