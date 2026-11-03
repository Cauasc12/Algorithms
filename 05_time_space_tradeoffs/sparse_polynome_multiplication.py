def sparse_polynome_multiplication(p, q):

    result = {}
    
    for (e1, c1) in p.items():
        for (e2, c2) in q.items():
            new_e = e1 + e2
            new_c = c1 * c2

            result[new_e] = result.get(new_e,0) + new_c

    filtered_result = {}
    for (e, c) in result.items():
        if c != 0:
            filtered_result[e] = c

    return filtered_result