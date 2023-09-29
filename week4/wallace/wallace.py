from sys import stdin

if __name__ == "__main__":
    n = int(next(stdin))
    weights = []
    results = [False]*2001
    results[0] = True

    for _ in range(n):
        weights.append(int(next(stdin)))

    for i, w in enumerate(weights):
        for j in range(2000,-1,-1):
            if results[j] and j+w <= 2000:
                results[j+w] = True
    
    if results[1000]:
        print(1000)
    else:
        for i in range(1, 1000):
            res1 = 1000-i
            res2 = 1000+i

            if results[res1] and results[res2]:
                print(res2)
                break

            if results[res1]:
                print(res1)
                break
            if results[res2]:
                print(res2)
                break

