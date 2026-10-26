def extreme_points(points):

    """Find the lexicographically smallest and largest points.
    
    Preconditions:
    Input must be a nonempty sequence of comparable numeric (x, y) pairs.
    
    Result:
    Return (minimum_point, maximum_point), prioritizing x and breaking
    ties by y. This is not the set of all four coordinate extrema.
    """
    p_min_x = points[0]
    p_max_x = points[0]

    for p in points:
        if p[0] < p_min_x[0] or (p[0] == p_min_x[0] and p[1] < p_min_x[1]):
            p_min_x = p
        if p[0] > p_max_x[0] or (p[0] == p_max_x[0] and p[1] > p_max_x[1]):
            p_max_x = p

    if p_min_x != p_max_x:
        return (p_min_x, p_max_x)
    
    p_min_y = points[0]
    p_max_y = points[0]

    for p in points:
        if p[1] < p_min_y[1] or (p[1] == p_min_y[1] and p[0] < p_min_y[0]):
            p_min_y = p
        if p[1] > p_max_y[1] or (p[1] == p_max_y[1] and p[0] > p_max_y[0]):
            p_max_y = p

    return (p_min_y, p_max_y)