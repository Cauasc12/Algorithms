def righ_left_exponentitation(a, n):
    product = 1
    term = a

    while n > 0:
        if n % 2 == 1:
            product *= term
        term *= term
        n //= 2

    return product