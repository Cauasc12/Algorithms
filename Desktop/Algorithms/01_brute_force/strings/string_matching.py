def string_matching(test, pattern):
    n = len(test)
    m = len(pattern)
    
    for i in range(n-m+1):
        j = 0
        while j < m and pattern[j] == test[i+j]:
            j += 1
        if j == m:
            return i
        
    return -1