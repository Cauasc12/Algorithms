def polynomial_evaluation(polynome, x):
    """Evaluate a polynomial from coefficients in increasing degree order.
    
    Preconditions:
    polynome is a nonempty sequence [a0, a1, ..., an] representing
    a0 + a1*x + ... + an*x**n. Coefficients and x support arithmetic.
    
    Result:
    Return the polynomial value; input is not modified.
    """
    n = len(polynome)
    p = polynome[0]
    xi = 1
    
    for i in range(1, n):
        xi *= x
        p = p + (polynome[i] * xi)
    
    return p
