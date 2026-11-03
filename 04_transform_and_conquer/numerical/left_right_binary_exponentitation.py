def left_right_binary_exponentitation(a, b):
    product = a

    for bit in b:
        product *= product
        if bit == 1:
            product *= a

    return product