from sys import stdin

if __name__ == "__main__":

    cap, cases = map(int, next(stdin))
    items = []

    for _ in cases:
        value, weight = map(int, next(stdin))
        items.append((value, weight))

    items.sort(key=lambda x : x[1]) # Sort the items based on the capacity

    

