from sys import stdin
from point import Point
import sys

# Goes through all the points and calculates the shortest dist between them.
# Returns the shortest distance pair
def compare_points(ps, n):
    current_min = (sys.float_info.max, (Point(0,0), Point(0,0)))

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

def get_mid_index(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n+1)//2

def get_points_close_to_line(maxl, minl, p, mid):
    new_p = p
    for i in range(mid, len(p)):
        if p[i].x > maxl:
            new_p = new_p[:i]
            break
    
    for i in range(mid-1, -1, -1):
        if p[i].x < minl:
            new_p = new_p[i+1:]
            break
    
    return new_p

def check_split_line(p, line_x, min_dist_pair, mid): 
    min_dist, _ = min_dist_pair
    max_line_x = line_x + min_dist
    min_line_x = line_x - min_dist

    S = get_points_close_to_line(max_line_x, min_line_x, p, mid) # Create set close to line
    S.sort(key=lambda a: a.y) # Sort on the y coordinate

    # Go through set and compare them
    n_sy = len(S)
    for i in range(n_sy-1): # Go through all the points except the last 
        pi = S[i]
        for j in range(i+1, min(n_sy, i+11)): # Pseudo code says go through the next 15 points 
            pj = S[j]
            pair = ((pi.distance(pj)), (pi,pj))
            min_dist_pair = min(min_dist_pair, pair, key=lambda x: x[0])

    return min_dist_pair

def closests_pair(p):

    n = len(p)
    if n <= 3:
        return compare_points(p, n) # Go through all the points and get the shortest dist pair

    mid_idx = get_mid_index(len(p))

    # Divide the sorted point sets in half
    pl = p[:mid_idx] # get left half og points
    pr = p[mid_idx:] # get right half of points
    L = p[mid_idx].x # Get the maximum x from the left set to form a line

    # Find the closest pair in set Q and R
    sl = closests_pair(pl) 
    sr = closests_pair(pr) 

    s =  min(sl, sr, key=lambda p : p[0]) # Get the pair with the lowest dist value

    return check_split_line(p, L, s, mid_idx)

if __name__ == "__main__":
    n = int(next(stdin))

    points = []
    for _ in range(n):
        x, y = map(float, next(stdin).split())
        points.append(Point(x,y))

    # Sort in x and y direction creating a set of x and y sorted points
    px = sorted(points, key=lambda p : p.x)
    _, shortest_points = closests_pair(px)

    p1, p2 = shortest_points

    print(p1.x, p1.y)
    print(p2.x, p2.y)