def right_left_binary_exponentitation(a, b):
    term = a
    product = 1

    for bit in b:
        term *= term
        if bit == 1:
            product *= term

    return product