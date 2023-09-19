from sys import stdin
from point import Point
import sys

sys.setrecursionlimit(10**6)
# Goes through all the points and calculates the shortest dist between them.
# Returns the shortest distance pair
def compare_points(ps, n):
    current_min = (100000000, (Point(0,0), Point(0,0)))

    for i in range(0, n-1):
        pi = ps[i]
        for j in range(i+1, n):
            pj = ps[j]
            new_d = pi.distance(pj)
            current_min = min(current_min, (new_d, (pi, pj)), key=lambda pair: pair[0])
    
    return current_min

# Splits a set of points on the x axis and returns the two halfs
def split_set_on_x(S, x):
    a = []
    b = []
    for s in S:
        if s.x <= x:
            a.append(s)
        else:
            b.append(s)
    
    return a, b

def check_split_line(py, line_x, min_dist_pair): 
    min_dist, pair = min_dist_pair
    max_line_x = line_x + min_dist
    min_line_x = line_x - min_dist

    sy = [p for p in py if min_line_x <= p.x <= max_line_x] # Create set close to line

    current_min_dist = min_dist
    current_min_pair = pair

    # Go through set and compare them
    n_sy = len(sy)
    for i in range(n_sy-1): # Go through all the points except the last 
        pi = sy[pi]
        for j in range(i+1, min(n_sy, i+15)): # Pseudo code says go through the next 15 points 
            pj = sy[j]
            dist = pi.distance(pj)
            if current_min_dist > dist:
                current_min_dist = dist
                current_min_pair = pi, pj

    return current_min_dist, current_min_pair

def closests_pair(px, py):

    n = len(px)
    if n <= 3:
        return compare_points(px, n) # Go through all the points and get the shortest dist pair

    mid_idx = len(points)//2

    # Divide the sorted point sets in half
    qx = px[:mid_idx] # get left half og points
    rx = px[mid_idx:] # get right half of points
    max_x = qx[-1].x # Get the maximum x to form a line
    qy, ry = split_set_on_x(py, max_x) # Get the lower and upper half of points

    # Find the closest pair in set Q and R
    pair1 = closests_pair(qx, qy) 
    pair2 = closests_pair(rx, ry) 

    s =  min(pair1, pair2, key=lambda p : p[0]) # Get the pair with the lowest dist value

    return check_split_line(py, max_x, s)

if __name__ == "__main__":
    n = int(next(stdin))

    points = []
    for _ in range(n):
        x, y = map(float, next(stdin).split())
        points.append(Point(x,y))

    # Sort in x and y direction creating a set of x and y sorted points
    px = sorted(points, key=lambda p : p.x)
    py = sorted(points, key=lambda p : p.y)
    _, shortest_points = closests_pair(px, py)

    p1, p2 = shortest_points

    print(p1.x, p1.y)
    print(p2.x, p2.y)