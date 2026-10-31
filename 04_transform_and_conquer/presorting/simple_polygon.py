import math

def simple_polygon(points):
    n = len(points)
    if n < 3:
        return 0

    p0 = min(points, key=lambda p: (p[1], p[0]))

    def angle(p):
        dx = p[0] - p0[0]
        dy = p[1] - p0[1]
        angle = math.atan2(dy,dx)
        dist = math.sqrt(dx**2 + dy**2)

        return (angle, dist)

    others = []
    for p in points:
        if p != p0:
            others.append(p)
    others = sorted(others,  key=angle())

    polygon = [p0] + others
    return polygon