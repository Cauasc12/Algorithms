def summation_game(sum, target, max_sum):
    """Choose an increment in a game of reaching a target sum.
    
    Preconditions:
    sum, target, and max_sum are integers with sum < target and
    max_sum >= 1. A move adds 1 through max_sum without exceeding
    the target; reaching it exactly wins.
    
    Result:
    Return a winning increment when possible; otherwise return 1.
    Do not call this function after the target is reached.
    """
    size = target - sum
    rest = size % (max_sum+1)

    if rest != 0:
        return rest
    else:
        return 1