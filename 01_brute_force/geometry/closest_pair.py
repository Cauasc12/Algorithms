import math

def closest_pair(points):
    """Compute the minimum Euclidean distance between two points.
    
    Preconditions:
    Points are numeric (x, y) pairs. Arithmetic must remain finite
    and accurate enough for distance comparisons. Duplicates are allowed.
    
    Result:
    Return the minimum distance, not the point pair. With fewer than
    two points return positive infinity.
    """
    n = len(points)
    d = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            xi, yi = points[i]
            xj, yj = points[j]
            distancia = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            d = min(d, distancia)
            
    return d