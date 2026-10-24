import math

def closest_pair(points):
    n = len(points)
    d = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            xi, yi = points[i]
            xj, yj = points[j]
            distancia = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            d = min(d, distancia)
            
    return d