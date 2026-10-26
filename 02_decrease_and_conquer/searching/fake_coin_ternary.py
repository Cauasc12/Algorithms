def weight(group1, group2):
    weight1 = 0
    for coin in group1:
        weight1 += coin[1]
    
    weight2 = 0
    for coin in group2:
        weight2 += coin[1]

    if weight1 <  weight2:
       return group1
    elif weight1 >  weight2:
        return group2
    
    return 1

def fake_coin_ternary(coins):
    """Find a lighter counterfeit coin using ternary reduction.
    
    Preconditions:
    Input must be a nonempty list of (identifier, weight) records with
    exactly one lighter coin; all genuine coins have equal weight.
    
    Result:
    Return the counterfeit coin record.
    """
    n = len(coins)

    if n == 1:
        return coins[n-1]
    
    k = n // 3
    if n == 2:
        k = 1
        
    group1 = coins[:k]
    group2 = coins[k:2*k]
    group3 = coins[2*k:] 

    result = weight(group1, group2)

    if result == group1:
        return fake_coin_ternary(group1)
    elif result == group2:
        return fake_coin_ternary(group2)
    else:
        return fake_coin_ternary(group3)
    