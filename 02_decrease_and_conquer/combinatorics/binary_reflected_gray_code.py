def binary_reflected_gray_code(number):

    """Generate binary reflected Gray code words.
    
    Preconditions:
    number must be an integer greater than or equal to 1.
    
    Result:
    Return 2**number distinct words of length number; consecutive words
    differ in one bit.
    """
    if(number == 1):
        return ["0", "1"]

    l1 = binary_reflected_gray_code(number-1)
    l2 =  l1[::-1]

    result_l1 = []
    for item in l1:
        result_l1.append("0" + item)

    result_l2 = []
    for item in l2:
        result_l2.append("1" + item)

    return result_l1 + result_l2