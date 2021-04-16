visited = []
res = []

def permutation(items, r, pos):
    if pos == r:
        print(res)
        return

    for item in items:
        if item not in visited:
            res.append(item)
            visited.append(item)
            permutation(items, r, pos+1)
            visited.pop()
            res.pop()

items = [1, 2, 3, 4, 5]
permutation(items, 2, 0)