def mdc(n,m):

    if m == 0:
        return n
    
    return mdc(m,n%m)

def mmc(n,m):

    if n == 0 or m == 0:
        return 0

    return (n*m) // mdc(n ,m)
    