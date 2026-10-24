def polynomial_evaluation(polynome, x):
    n = len(polynome)
    p = polynome[0]
    xi = 1
    
    for i in range(1, n):
        xi *= x
        p = p + (polynome[i] * xi)
    
    return p
