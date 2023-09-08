# This is a solution to the interval scheduling problem 
# from kattis ITU: https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2023/assignments/mp7x8i/problems/intervalscheduling

from sys import stdin

def snd(e):
    return e[1]

n = int(next(stdin))
events = []

for _ in range(n):
    s,f = map(int, next(stdin).split())
    events.append((s,f))

events.sort(key=snd)

current_event = events.pop(0)
result = 1

for i in range(len(events)):
    e = events[i]

    if e[0] >= current_event[1]:
        result += 1
        current_event = e

print(result)