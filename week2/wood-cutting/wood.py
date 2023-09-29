# This code solves the "wood cutting" problem from ITU Kattis: https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2023/assignments/mp7x8i/problems/woodcutting
from sys import stdin

cases = int(next(stdin))

for _ in range(cases):
    n = int(next(stdin)) # Number of customers in the test case
    customers = []
    for _ in range(n):
        wood = list(map(int, next(stdin).split()))
        wood.pop(0)
        customers.append(sum(wood))
    
    customers.sort()
    timeTaken = 0
    result = 0

    for i in customers:
        timeTaken += i
        result += timeTaken
    
    print(result / len(customers))

