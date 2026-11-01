def max_points(points):

    points_sorted = sorted(points, key=lambda p: p[0], reverse=True)
    n = len(points_sorted)

    if n == 0:
        return []

    y_max = float('-inf')
    max_points = []
    
    for p in points_sorted:
        if p[1] > y_max:
            y_max = p[1]
            max_points.append(p)

    return max_points